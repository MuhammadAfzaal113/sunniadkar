from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import authenticate as login_auth
from nameparser import HumanName
from validators.email import email as email_validator

from apps.user.models import User
from apps.utils.jwt_config import get_jwt_token


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    try:
        if request.data.get('email') and request.data.get('password'):
            if email_validator(request.data.get('email')) is not True:
                return Response({'success': True, 'message': 'Email is not valid'},
                                status=status.HTTP_400_BAD_REQUEST)

            User.objects.create_user(
                email=request.data['email'],
                password=request.data['password'],
                full_name=request.data['full_name'],
                address=request.data.get('address'),
                lat_long=request.data.get('lat_long')
            )
            return Response({'success': True, 'message': 'User created successfully.'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'success': False, 'message': 'Email and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError as e:
        return Response({'success': False, 'message': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    try:
        if request.data.get('email') and request.data.get('password'):
            if email_validator(request.data.get('email')) is not True:
                return Response({'success': True, 'message': 'Email is not valid'},
                                status=status.HTTP_400_BAD_REQUEST)

            user = login_auth(email=str(request.data.get('email')).lower(), password=request.data.get('password'))

            if user:
                if not user.is_active:
                    return Response({
                        'success': False,
                        'message': 'User is inactive/deleted, please contact your admin for further details.'},
                        status=status.HTTP_400_BAD_REQUEST)

                tokens = get_jwt_token(user)
                full_name = HumanName(str(user.full_name))

                response = {
                    'success': True,
                    'message': 'Login successfully',
                    'accessToken': tokens['accessToken'],
                    'refreshToken': tokens['refreshToken'],
                    'user_id': str(user.id),
                    'email': user.email,
                    'first_name': full_name.first if full_name else "",
                    'last_name': full_name.last if full_name else "",
                    'address': user.address
                }

                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'message': 'Invalid credentials.'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'message': 'Email and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    try:
        user = User.objects.get(id=request.user.id)
        full_name = HumanName(str(user.full_name))

        response = {
            'success': True,
            'message': 'User profile fetched successfully',
            'user_id': str(user.id),
            'email': user.email,
            'first_name': full_name.first if full_name else "",
            'last_name': full_name.last if full_name else "",
            'address': user.address
        }
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
