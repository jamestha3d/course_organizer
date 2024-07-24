from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()

# account_activation_token.check_token(user, token)
# account_activation_token.make_token(user)
#uid = force_str(urlsafe_base64_decode(uidb64)) #decode user. retrieve from verification link
#urlsafe_base64_encode(force_bytes(user.pk)) #encode user. use this as part of verification link