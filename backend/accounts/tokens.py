from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

TOKEN_VALIDITY_PERIOD = settings.ACTIVATION_TOKEN_EXPIRE_HOURS or 24
User = get_user_model()

def create_jwt_pair_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    tokens={
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }

    return tokens

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        expiration_time = timezone.now() + timedelta(hours=TOKEN_VALIDITY_PERIOD)
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active) + six.text_type(expiration_time)
        )


    def check_token(self, user, token):
        try:
            # Check if the token is expired
            if self._get_token_timestamp(token) < timezone.now() - timedelta(hours=TOKEN_VALIDITY_PERIOD):
                return False
            return super().check_token(user, token)
        except Exception:
            return False

    def _get_token_timestamp(self, token):
        # Extract timestamp from token
        # This is a simplified example; you need to properly parse your token
        return timezone.datetime.strptime(token.split(":")[1], "%Y-%m-%d %H:%M:%S")
    

account_activation_token = AccountActivationTokenGenerator()

# account_activation_token.check_token(user, token)
# account_activation_token.make_token(user)
#uid = force_str(urlsafe_base64_decode(uidb64)) #decode user. retrieve from verification link
#urlsafe_base64_encode(force_bytes(user.pk)) #encode user. use this as part of verification link