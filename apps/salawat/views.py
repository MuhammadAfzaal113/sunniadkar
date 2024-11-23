from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.user.models import User
from apps.salawat.models import Salawat


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_salawat_view(request):
    try:
        if not request.data.get('salawat_title') or not request.data.get('salawat_text'):
            return Response({'success': False, 'message': 'Salawat title and description are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        salwat_object = Salawat.objects.create(
            salawat_title=request.data.get('salawat_title'),
            salawat_text=request.data.get('salawat_text'),
        )
        response_data = {
            'success': True,
            'message': 'Salawat created successfully.',
            'id': str(salwat_object.id),
            'salawat_title': salwat_object.salawat_title,
            'salawat_text': salwat_object.salawat_text
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        return Response({'success': False, 'message': 'Salawat already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_salawat_view(request):
    try:
        salawat = Salawat.objects.all()
        response_data = {
            'success': True,
            'message': 'Salawat fetched successfully.',
            'salawat': salawat
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_salawat_by_id_view(request, id):
    try:
        salawat = Salawat.objects.get(id=id)
        response_data = {
            'success': True,
            'message': 'Salawat fetched successfully.',
            'salawat': salawat
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_salawat_view(request, id):
    try:
        salawat = Salawat.objects.get(id=id)
        salawat.delete()
        return Response({'success': True, 'message': 'Salawat deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_salawat_view(request, id):
    try:
        if not request.data.get('salawat_title') or not request.data.get('salawat_text'):
            return Response({'success': False, 'message': 'Salawat title and description are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        salawat = Salawat.objects.get(id=id)
        salawat.salawat_title = request.data.get('salawat_title')
        salawat.salawat_text = request.data.get('salawat_text')
        salawat.save()
        return Response({'success': True, 'message': 'Salawat updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_random_salawat_view(request):
    try:
        salawat = Salawat.objects.order_by('?').first()
        response_data = {
            'success': True,
            'message': 'Salawat fetched successfully.',
            'salawat': salawat
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)