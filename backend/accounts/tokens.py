from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
from django.utils.http import base36_to_int, int_to_base36
from django.utils.crypto import constant_time_compare
import jwt

TOKEN_VALIDITY_PERIOD = settings.ACTIVATION_TOKEN_EXPIRE_HOURS or 48 * 3600
User = get_user_model()

def create_jwt_pair_for_user(user: User): # type: ignore
    refresh = RefreshToken.for_user(user)

    tokens={
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }

    return tokens

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_activated)
        )
    
account_activation_token = AccountActivationTokenGenerator()


class LoginTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.last_login)
        )

login_token_generator = LoginTokenGenerator()


# account_activation_token.check_token(user, token)
# account_activation_token.make_token(user)
#uid = force_str(urlsafe_base64_decode(uidb64)) #decode user. retrieve from verification link
#urlsafe_base64_encode(force_bytes(user.pk)) #encode user. use this as part of verification link

def decode_jwt_token(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

def create_state_token(state):
    payload = {
        'state': state,
        'exp': datetime.utcnow() + timedelta(minutes=10)  # State token expires in 10 minutes
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def create_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')