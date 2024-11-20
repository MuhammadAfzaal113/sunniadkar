from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.user.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    try:
        if request.data.get('email') and request.data.get('password'):
            User.objects.create_user(email=request.data.get('email'), password=request.data.get('password'))
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
            user = User.objects.get(email=request.data.get('email'))
            if user.check_password(request.data.get('password')):
                data = {
                    'user_id': str(user.id),
                    'email': user.email,
                    'full_name': user.full_name
                }
                return Response({'success': True, 'message': 'User logged in successfully.'},
                                status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'message': 'Invalid credentials.'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'message': 'Email and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

