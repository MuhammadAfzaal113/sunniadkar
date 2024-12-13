from rest_framework_simplejwt.tokens import RefreshToken


def get_jwt_token(user):
    """Function for jwt access and refresh token"""
    refresh = RefreshToken.for_user(user)

    return {
        'refreshToken': str(refresh),
        'accessToken': str(refresh.access_token)
    }
