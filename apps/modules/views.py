from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.user.models import User
from apps.modules.models import Salawat, DuaCategory, Dua, Books
from itertools import groupby
from operator import itemgetter


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
@permission_classes([AllowAny])
def get_salawat_view(request):
    try:
        salawat = Salawat.objects.all().values()
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


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dua_category_view(request):
    try:
        dua_category = DuaCategory.objects.all().values()
        response_data = {
            'success': True,
            'message': 'Dua category fetched successfully.',
            'dua_category': dua_category
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dua_category_by_id_view(request, id):
    try:
        dua_category = DuaCategory.objects.get(id=id)
        response_data = {
            'success': True,
            'message': 'Dua category fetched successfully.',
            'dua_category': dua_category
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_dua_category_view(request):
    try:
        if not request.data.get('dua_category_name'):
            return Response({'success': False, 'message': 'Dua category name is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        dua_category_object = DuaCategory.objects.create(
            dua_category_name=request.data.get('dua_category_name'),
        )
        response_data = {
            'success': True,
            'message': 'Dua category created successfully.',
            'id': str(dua_category_object.id),
            'dua_category_name': dua_category_object.dua_category_name,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        return Response({'success': False, 'message': 'Dua category already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_dua_category_view(request, id):
    try:
        dua_category = DuaCategory.objects.get(id=id)
        dua_category.delete()
        return Response({'success': True, 'message': 'Dua category deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_dua_category_view(request, id):
    try:
        if not request.data.get('dua_category_name'):
            return Response({'success': False, 'message': 'Dua category name is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        dua_category = DuaCategory.objects.get(id=id)
        dua_category.dua_category_name = request.data.get('dua_category_name')
        dua_category.save()
        return Response({'success': True, 'message': 'Dua category updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dua_view_by_category_view(request):
    try:
        dua_objects = Dua.objects.filter(category=request.query_params.get('dua_category_id')).values()

        # Group by category_id
        dua_objects = sorted(dua_objects, key=itemgetter('category_id'))  # Sort before grouping
        grouped = groupby(dua_objects, key=itemgetter('category_id'))

        result = []
        for category_id, duas in grouped:
            # Get the category name (assume it's fetched from another query or cached)
            category_name = DuaCategory.objects.get(id=category_id).category_name
            result.append({
                "category_name": category_name,
                "category_id": category_id,
                "dua": list(duas)
            })

        response_data = {
            'success': True,
            'message': 'Dua fetched successfully.',
            'dua': result
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dua_by_id_view(request, id):
    try:
        dua = Dua.objects.get(id=id)
        response_data = {
            'success': True,
            'message': 'Dua fetched successfully.',
            'dua': dua
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_book_view(request):
    try:
        book = Books.objects.all().values()
        response_data = {
            'success': True,
            'message': 'Book fetched successfully.',
            'book': book
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
