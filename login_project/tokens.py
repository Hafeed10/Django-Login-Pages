from django.contrib.auth.tokens import PasswordResetTokenGenerator

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp)
            # Uncomment and modify the following line if you have a profile model with signup_confirmation
            # + str(user.profile.signup_confirmation)
        )

generate_token = TokenGenerator()
