from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User
from apis.models import Institution
from apis.serializers import InstitutionSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class SignUpSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    #username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['email', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password) #calling set password here as the set password in create in models does not get called when we use serializer
        user.save()
        Token.objects.create(user=user)
        return user
    

class InstitutionSignupSerializer(serializers.ModelSerializer):
    
    institution_name = serializers.CharField(write_only=True)
    type = serializers.CharField(write_only=True)

    
    def validate_institution_name(self,value):
        serializer = InstitutionSerializer(data={"name": value})
        if serializer.is_valid():
            return value
        else:
            raise ValidationError(serializer.errors)
    
    def validate_type(self,value):
        serializer = InstitutionSerializer(data={"type": value})
        if serializer.is_valid():
            return value
        else:
            raise ValidationError(serializer.errors)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'institution_name', 'type']


    def create(self, validated_data):

        print(validated_data)
        name = validated_data.pop('institution_name')
        type = validated_data.pop('type')
        institution = Institution.objects.create(name=name, type=type)
        user = User(
            first_name = validated_data.get("first_name"),
            last_name = validated_data.get("last_name"),
            email = validated_data.get("email"),
            institution = institution,
            role = User.ROLES.SUPER_ADMIN
        )

        user.set_password(validated_data['password'])
        user.save()

        

        return institution, user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['institution'] = str(user.institution.pk)
        # ...

        return token
    
