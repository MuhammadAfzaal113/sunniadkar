from django.http import JsonResponse
from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.user.models import User
from apps.modules.models import *
from itertools import groupby
from operator import itemgetter

@api_view(['GET'])
@permission_classes([AllowAny])
def get_salawat_view(request):
    try:
        id = request.query_params.get('id', None)
        if id:
            salawat = Salawat.objects.filter(id=id).values('id', 'title', 'description').first()
            response_data = {
                'success': True,
                'message': 'Salawat fetched successfully.',
                'salawat': salawat
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            salawat = Salawat.objects.values('id', 'title', 'description').order_by('-created_at')
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
        id = request.query_params.get('id', None)
        if id:
            dua_category = DuaCategory.objects.filter(id=id).values('id', 'category_name').first()
            response_data = {
                'success': True,
                'message': 'Dua category fetched successfully.',
                'dua_category': dua_category
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            dua_category = DuaCategory.objects.values('id', 'category_name').order_by('-created_at')
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
def get_dua_view_by_category_view(request):
    try:
        if request.query_params.get('dua_category_id'):
            dua_objects = Dua.objects.filter(category=request.query_params.get('dua_category_id')).values()
        else:
            dua_objects = Dua.objects.values()

        # Group by category_id
        dua_objects = [obj for obj in dua_objects if obj['category_id'] is not None]
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
        book = Books.objects.values('id', 'title', 'description', 'link').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Book fetched successfully.',
            'book': book
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_mewlid(request):
    try:
        mewlid = Mewlid.objects.values('id', 'title', 'description').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Mewlid fetched successfully.',
            'mewlid': mewlid
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Mewlid because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_qasida(request):
    try:
        qasida = Qasida.objects.values('id', 'title', 'description').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Qasida fetched successfully.',
            'qasida': qasida
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Qasida because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_lecture(request):
    try:
        lecture = Lecture.objects.values('id', 'title', 'link').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Lecture fetched successfully.',
            'lecture': lecture
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Lecture because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_article(request):
    try:
        article = Article.objects.values('id', 'title', 'description', 'link').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Article fetched successfully.',
            'article': article
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Article because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_qa(request):
    try:
        qa = QA.objects.values('id', 'question', 'answer').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'QA fetched successfully.',
            'qa': qa
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch QA because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_download(request):
    try:
        download = Download.objects.values('id', 'title', 'link').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Download fetched successfully.',
            'download': download
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Download because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_marriage_guide(request):
    try:
        marriage_guide = MarriageGuide.objects.values('id', 'title', 'description', 'link').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Marriage Guide fetched successfully.',
            'marriage_guide': marriage_guide
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Marriage Guide because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_pledge_salawat(request):
    try:
        if request.query_params.get('campaign', None):
            pledge_salawat = PledgeSalawat.objects.filter(campaign=request.query_params.get('campaign', None)).values('created_at', 'campaign', 'name', 'address', 'salat', 'pledge_count').order_by('-created_at')
        else:
            pledge_salawat = PledgeSalawat.objects.values('created_at', 'campaign', 'name', 'address', 'salat', 'pledge_count').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Pledge Salawat fetched successfully.',
            'total_pledge_salawat': pledge_salawat.count() if pledge_salawat else 0,
            'pledge_salawat': pledge_salawat,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Pledge Salawat because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_pledge_salawat(request):
    try:
        data = request.data

        if not data.get('amount', None):
            return Response({'success': False, 'message': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('name', None):
            return Response({'success': False, 'message': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('campaign', None):
            return Response({'success': False, 'message': 'Campaign is required.'}, status=status.HTTP_400_BAD_REQUEST)

        PledgeSalawat.objects.create(
            campaign=data.get('campaign', None),
            amount=data.get('amount', None),
            name=data.get('name', None),
            address=data.get('address', None),
            salat=data.get('salat', None),
        )
        return Response({'success': True, 'message': 'Pledge Salawat created successfully.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_community_category(request):
    try:
        community_category = CommunityCategory.objects.values('id', 'category_name').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Community Category fetched successfully.',
            'community_category': community_category
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Community Category because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_community(request):
    try:
        community = Community.objects.values('id', 'name', 'address', 'description', 'like', 'dua', 'ameen').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Community fetched successfully.',
            'community': community
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Community because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_LifeLesson(request):
    try:
        life_lesson = LifeLesson.objects.values('id', 'author__full_name', 'description').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Life Lesson fetched successfully.',
            'life_lesson': life_lesson
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Life Lesson because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_community(request):
    try:
        data = request.data
        
        Community.objects.create(
            name= data.get('name', 'Guest'),
            address=data.get('address', None),
            description=data.get('description', None),
        )
        
        return Response({'success': True, 'message': 'Community created successfully.'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def like_post(request):
    try:
        id = request.data.get('id', None)
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_200_OK)


        community = Community.objects.get(id=id)
        if not community:
            return Response({'success': False, 'message': 'Community not found.'}, status=status.HTTP_200_OK)

        community.like += 1
        community.save()
        return Response({'success': True, 'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def dua_post(request):
    try:
        id = request.data.get('id', None)
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_200_OK)

        community = Community.objects.get(id=id)
        if not community:
            return Response({'success': False, 'message': 'Community not found.'}, status=status.HTTP_200_OK)

        community.dua += 1
        community.save()
        return Response({'success': True, 'message': 'Post Dua successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([AllowAny])
def ameen_post(request):
    try:
        id = request.data.get('id', None)
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_200_OK)

        community = Community.objects.get(id=id)
        if not community:
            return Response({'success': False, 'message': 'Community not found.'}, status=status.HTTP_200_OK)
        community.ameen += 1
        community.save()
        return Response({'success': True, 'message': 'Post Ameen successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_campaign_list(request):
    try:
        campaign = Campaign.objects.values('id', 'name').order_by('-created_at')
        for camp in campaign:
            camp['pledge_user_count'] = PledgeSalawat.objects.filter(campaign=camp['id']).count()
        response_data = {
            'success': True,
            'message': 'Campaign fetched successfully.',
            'campaign': campaign
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Campaign because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_mentality_booster(request):
    try:
        mentality_booster = MentalityBooster.objects.values('id', 'title', 'description').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Mentality Booster fetched successfully.',
            'mentality_booster': mentality_booster
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Mentality Booster because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_health_tips(request):
    try:
        health_tips = HealthTips.objects.values('id', 'title', 'description').order_by('-created_at')
        response_data = {
            'success': True,
            'message': 'Health Tips fetched successfully.',
            'health_tips': health_tips
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Health Tips because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_pathway(request):
    try:
        pathway = Pathway.objects.values('id', 'title', 'description').order_by('title')
        response_data = {
            'success': True,
            'message': 'Pathway fetched successfully.',
            'pathway': pathway
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Pathway because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_sister_section(request):
    try:
        sister_section = SisterSection.objects.values('id', 'title', 'description').order_by('title')
        response_data = {
            'success': True,
            'message': 'Sister Section fetched successfully.',
            'sister_section': sister_section
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': f"Failed to fetch Sister Section because : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    

#------------------------------------------ ADMIN API ---------------------------------------------------------
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_salawat(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        salawat = Salawat.objects.create(
            title=data.get('title'),
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Salawat created successfully.', 'salawat': salawat.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_salawat(request):
    try:
        data = request.data
        
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        salawat = Salawat.objects.filter(id=id).first()
        if not salawat:
            return Response({'success': False, 'message': 'Salawat not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        salawat.title = data.get('title', salawat.title)
        salawat.description = data.get('description', salawat.description)
        salawat.save()
        return Response({'success': True, 'message': 'Salawat updated successfully.'}, status=status.HTTP_200_OK)
    except Salawat.DoesNotExist:
        return Response({'success': False, 'message': 'Salawat not found.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_salawat(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        salawat = Salawat.objects.filter(id=id).first()
        if not salawat:
            return Response({'success': False, 'message': 'Salawat not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        salawat.delete()
        return Response({'success': True, 'message': 'Salawat deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_dua_category(request):
    try:
        data = request.data
        if not data.get('category_name'):
            return Response({'success': False, 'message': 'Category name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        dua_category = DuaCategory.objects.create(
            category_name=data.get('category_name'),
            created_by=request.user  # Assuming `created_by` is set to the logged-in admin user
        )
        return Response({'success': True, 'message': 'Dua category created successfully.', 'dua_category': dua_category.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_dua_category(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('category_name'):
            return Response({'success': False, 'message': 'Category name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        dua_category = DuaCategory.objects.filter(id=id).first()
        if not dua_category:
            return Response({'success': False, 'message': 'Dua category not found.'}, status=status.HTTP_400_BAD_REQUEST)

        dua_category.category_name = data.get('category_name', dua_category.category_name)
        dua_category.save()
        return Response({'success': True, 'message': 'Dua category updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_dua_category(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        dua_category = DuaCategory.objects.filter(id=id).first()
        if not dua_category:
            return Response({'success': False, 'message': 'Dua category not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        dua_category.delete()
        return Response({'success': True, 'message': 'Dua category deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_dua(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        category_id = data.get('category')
        if not category_id:
            return Response({'success': False, 'message': 'Category is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        category = DuaCategory.objects.filter(id=category_id).first()
        if not category:
            return Response({'success': False, 'message': 'Category not found.'}, status=status.HTTP_400_BAD_REQUEST)

        dua = Dua.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            category=category,
            created_by=request.user  # Assuming `created_by` is set to the logged-in admin user
        )
        return Response({'success': True, 'message': 'Dua created successfully.', 'dua': dua.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_dua(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        dua = Dua.objects.filter(id=id).first()
        if not dua:
            return Response({'success': False, 'message': 'Dua not found.'}, status=status.HTTP_400_BAD_REQUEST)

        category_id = data.get('category')
        category = None
        if category_id:
            category = DuaCategory.objects.filter(id=category_id).first()
            if not category:
                return Response({'success': False, 'message': 'Category not found.'}, status=status.HTTP_400_BAD_REQUEST)

        dua.title = data.get('title', dua.title)
        dua.description = data.get('description', dua.description)
        dua.category = category
        dua.save()
        return Response({'success': True, 'message': 'Dua updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_dua(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        dua = Dua.objects.filter(id=id).first()
        if not dua:
            return Response({'success': False, 'message': 'Dua not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        dua.delete()
        return Response({'success': True, 'message': 'Dua deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_book(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description') or not data.get('link'):
            return Response({'success': False, 'message': 'Title, description, and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        book = Books.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            link=data.get('link'),
            created_by=request.user  # Assuming `created_by` is set to the logged-in admin user
        )
        return Response({'success': True, 'message': 'Book created successfully.', 'book': book.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_book(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description') or not data.get('link'):
            return Response({'success': False, 'message': 'Title, description, and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        book = Books.objects.filter(id=id).first()
        if not book:
            return Response({'success': False, 'message': 'Book not found.'}, status=status.HTTP_400_BAD_REQUEST)

        book.title = data.get('title', book.title)
        book.description = data.get('description', book.description)
        book.link = data.get('link', book.link)
        book.save()
        return Response({'success': True, 'message': 'Book updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_book(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        book = Books.objects.filter(id=id).first()
        if not book:
            return Response({'success': False, 'message': 'Book not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        book.delete()
        return Response({'success': True, 'message': 'Book deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_mewlid(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        mewlid = Mewlid.objects.create(
            title=data.get('title'),
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Mewlid created successfully.', 'mewlid': mewlid.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_mewlid(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        mewlid = Mewlid.objects.filter(id=id).first()
        if not mewlid:
            return Response({'success': False, 'message': 'Mewlid not found.'}, status=status.HTTP_400_BAD_REQUEST)

        mewlid.title = data.get('title', mewlid.title)
        mewlid.description = data.get('description', mewlid.description)
        mewlid.save()
        return Response({'success': True, 'message': 'Mewlid updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_mewlid(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mewlid = Mewlid.objects.filter(id=id).first()
        if not mewlid:
            return Response({'success': False, 'message': 'Mewlid not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mewlid.delete()
        return Response({'success': True, 'message': 'Mewlid deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_qasida(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        qasida = Qasida.objects.create(
            title=data.get('title', None),
            description=data.get('description', None)
        )
        return Response({'success': True, 'message': 'Qasida created successfully.', 'qasida': qasida.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_qasida(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        qasida = Qasida.objects.filter(id=id).first()
        if not qasida:
            return Response({'success': False, 'message': 'Qasida not found.'}, status=status.HTTP_400_BAD_REQUEST)

        qasida.title = data.get('title', qasida.title)
        qasida.description = data.get('description', qasida.description)
        qasida.save()
        return Response({'success': True, 'message': 'Qasida updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_qasida(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        qasida = Qasida.objects.filter(id=id).first()
        if not qasida:
            return Response({'success': False, 'message': 'Qasida not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        qasida.delete()
        return Response({'success': True, 'message': 'Qasida deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_lecture(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('link'):
            return Response({'success': False, 'message': 'Title and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        lecture = Lecture.objects.create(
            title=data.get('title'),
            link=data.get('link')
        )
        return Response({'success': True, 'message': 'Lecture created successfully.', 'lecture': lecture.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_lecture(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('link'):
            return Response({'success': False, 'message': 'Title and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        lecture = Lecture.objects.filter(id=id).first()
        if not lecture:
            return Response({'success': False, 'message': 'Lecture not found.'}, status=status.HTTP_400_BAD_REQUEST)

        lecture.title = data.get('title', lecture.title)
        lecture.link = data.get('link', lecture.link)
        lecture.save()
        return Response({'success': True, 'message': 'Lecture updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_lecture(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        lecture = Lecture.objects.filter(id=id).first()
        if not lecture:
            return Response({'success': False, 'message': 'Lecture not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        lecture.delete()
        return Response({'success': True, 'message': 'Lecture deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_article(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description') or not data.get('link'):
            return Response({'success': False, 'message': 'Title, description, and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        article = Article.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            link=data.get('link')
        )
        return Response({'success': True, 'message': 'Article created successfully.', 'article': article.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_article(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description') or not data.get('link'):
            return Response({'success': False, 'message': 'Title, description, and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        article = Article.objects.filter(id=id).first()
        if not article:
            return Response({'success': False, 'message': 'Article not found.'}, status=status.HTTP_400_BAD_REQUEST)

        article.title = data.get('title', article.title)
        article.description = data.get('description', article.description)
        article.link = data.get('link', article.link)
        article.save()
        return Response({'success': True, 'message': 'Article updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_article(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        article = Article.objects.filter(id=id).first()
        if not article:
            return Response({'success': False, 'message': 'Article not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        article.delete()
        return Response({'success': True, 'message': 'Article deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_qa(request):
    try:
        data = request.data
        if not data.get('question') or not data.get('answer'):
            return Response({'success': False, 'message': 'Question and answer are required.'}, status=status.HTTP_400_BAD_REQUEST)

        qa = QA.objects.create(
            question=data.get('question'),
            answer=data.get('answer')
        )
        return Response({'success': True, 'message': 'QA created successfully.', 'qa': qa.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_qa(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('question') or not data.get('answer'):
            return Response({'success': False, 'message': 'Question and answer are required.'}, status=status.HTTP_400_BAD_REQUEST)

        qa = QA.objects.filter(id=id).first()
        if not qa:
            return Response({'success': False, 'message': 'QA not found.'}, status=status.HTTP_400_BAD_REQUEST)

        qa.question = data.get('question', qa.question)
        qa.answer = data.get('answer', qa.answer)
        qa.save()
        return Response({'success': True, 'message': 'QA updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_qa(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        qa = QA.objects.filter(id=id).first()
        if not qa:
            return Response({'success': False, 'message': 'QA not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        qa.delete()
        return Response({'success': True, 'message': 'QA deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_download(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('link'):
            return Response({'success': False, 'message': 'Title and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        download = Download.objects.create(
            title=data.get('title'),
            link=data.get('link')
        )
        return Response({'success': True, 'message': 'Download created successfully.', 'download': download.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_download(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('link'):
            return Response({'success': False, 'message': 'Title and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        download = Download.objects.filter(id=id).first()
        if not download:
            return Response({'success': False, 'message': 'Download not found.'}, status=status.HTTP_400_BAD_REQUEST)

        download.title = data.get('title', download.title)
        download.link = data.get('link', download.link)
        download.save()
        return Response({'success': True, 'message': 'Download updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_download(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        download = Download.objects.filter(id=id).first()
        if not download:
            return Response({'success': False, 'message': 'Download not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        download.delete()
        return Response({'success': True, 'message': 'Download deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_marriage_guide(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description') or not data.get('link'):
            return Response({'success': False, 'message': 'Title, description, and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        marriage_guide = MarriageGuide.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            link=data.get('link')
        )
        return Response({'success': True, 'message': 'Marriage guide created successfully.', 'marriage_guide': marriage_guide.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_marriage_guide(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description') or not data.get('link'):
            return Response({'success': False, 'message': 'Title, description, and link are required.'}, status=status.HTTP_400_BAD_REQUEST)

        marriage_guide = MarriageGuide.objects.filter(id=id).first()
        if not marriage_guide:
            return Response({'success': False, 'message': 'Marriage guide not found.'}, status=status.HTTP_400_BAD_REQUEST)

        marriage_guide.title = data.get('title', marriage_guide.title)
        marriage_guide.description = data.get('description', marriage_guide.description)
        marriage_guide.link = data.get('link', marriage_guide.link)
        marriage_guide.save()
        return Response({'success': True, 'message': 'Marriage guide updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_marriage_guide(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        marriage_guide = MarriageGuide.objects.filter(id=id).first()
        if not marriage_guide:
            return Response({'success': False, 'message': 'Marriage guide not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        marriage_guide.delete()
        return Response({'success': True, 'message': 'Marriage guide deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_life_lesson(request):
    try:
        data = request.data
        if not data.get('description'):
            return Response({'success': False, 'message': 'Author and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        life_lesson = LifeLesson.objects.create(
            author=request.user,
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Life lesson created successfully.', 'life_lesson': life_lesson.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_life_lesson(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        life_lesson = LifeLesson.objects.filter(id=id).first()
        if not life_lesson:
            return Response({'success': False, 'message': 'Life lesson not found.'}, status=status.HTTP_400_BAD_REQUEST)

        life_lesson.author_id = data.get('author', life_lesson.author_id)
        life_lesson.description = data.get('description', life_lesson.description)
        life_lesson.save()
        return Response({'success': True, 'message': 'Life lesson updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_life_lesson(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        life_lesson = LifeLesson.objects.filter(id=id).first()
        if not life_lesson:
            return Response({'success': False, 'message': 'Life lesson not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        life_lesson.delete()
        return Response({'success': True, 'message': 'Life lesson deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_campaign(request):
    try:
        data = request.data
        if not data.get('name'):
            return Response({'success': False, 'message': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        campaign = Campaign.objects.create(
            name=data.get('name')
        )
        return Response({'success': True, 'message': 'Campaign created successfully.', 'campaign': campaign.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_campaign(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('name'):
            return Response({'success': False, 'message': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        campaign = Campaign.objects.filter(id=id).first()
        if not campaign:
            return Response({'success': False, 'message': 'Campaign not found.'}, status=status.HTTP_400_BAD_REQUEST)

        campaign.name = data.get('name', campaign.name)
        campaign.save()
        return Response({'success': True, 'message': 'Campaign updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_campaign(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        campaign = Campaign.objects.filter(id=id).first()
        if not campaign:
            return Response({'success': False, 'message': 'Campaign not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        campaign.delete()
        return Response({'success': True, 'message': 'Campaign deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_community_category(request):
    try:
        data = request.data
        if not data.get('category_name'):
            return Response({'success': False, 'message': 'Category name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        community_category = CommunityCategory.objects.create(
            category_name=data.get('category_name')
        )
        return Response({'success': True, 'message': 'Community category created successfully.', 'community_category': community_category.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_community_category(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('category_name'):
            return Response({'success': False, 'message': 'Category name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        community_category = CommunityCategory.objects.filter(id=id).first()
        if not community_category:
            return Response({'success': False, 'message': 'Community category not found.'}, status=status.HTTP_400_BAD_REQUEST)

        community_category.category_name = data.get('category_name', community_category.category_name)
        community_category.save()
        return Response({'success': True, 'message': 'Community category updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_community_category(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        community_category = CommunityCategory.objects.filter(id=id).first()
        if not community_category:
            return Response({'success': False, 'message': 'Community category not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        community_category.delete()
        return Response({'success': True, 'message': 'Community category deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_mentality_booster(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        mentality_booster = MentalityBooster.objects.create(
            title=data.get('title'),
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Mentality booster created successfully.', 'mentality_booster': mentality_booster.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_mentality_booster(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        mentality_booster = MentalityBooster.objects.filter(id=id).first()
        if not mentality_booster:
            return Response({'success': False, 'message': 'Mentality booster not found.'}, status=status.HTTP_400_BAD_REQUEST)

        mentality_booster.title = data.get('title', mentality_booster.title)
        mentality_booster.description = data.get('description', mentality_booster.description)
        mentality_booster.save()
        return Response({'success': True, 'message': 'Mentality booster updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_mentality_booster(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mentality_booster = MentalityBooster.objects.filter(id=id).first()
        if not mentality_booster:
            return Response({'success': False, 'message': 'Mentality booster not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mentality_booster.delete()
        return Response({'success': True, 'message': 'Mentality booster deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_health_tips(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        health_tips = HealthTips.objects.create(
            title=data.get('title'),
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Health tips created successfully.', 'health_tips': health_tips.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_health_tips(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        health_tips = HealthTips.objects.filter(id=id).first()
        if not health_tips:
            return Response({'success': False, 'message': 'Health tips not found.'}, status=status.HTTP_400_BAD_REQUEST)

        health_tips.title = data.get('title', health_tips.title)
        health_tips.description = data.get('description', health_tips.description)
        health_tips.save()
        return Response({'success': True, 'message': 'Health tips updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_health_tips(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        health_tips = HealthTips.objects.filter(id=id).first()
        if not health_tips:
            return Response({'success': False, 'message': 'Health tips not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        health_tips.delete()
        return Response({'success': True, 'message': 'Health tips deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_pathway(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        pathway = Pathway.objects.create(
            title=data.get('title'),
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Pathway created successfully.', 'pathway': pathway.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_pathway(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        pathway = Pathway.objects.filter(id=id).first()
        if not pathway:
            return Response({'success': False, 'message': 'Pathway not found.'}, status=status.HTTP_400_BAD_REQUEST)

        pathway.title = data.get('title', pathway.title)
        pathway.description = data.get('description', pathway.description)
        pathway.save()
        return Response({'success': True, 'message': 'Pathway updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_pathway(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        pathway = Pathway.objects.filter(id=id).first()
        if not pathway:
            return Response({'success': False, 'message': 'Pathway not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        pathway.delete()
        return Response({'success': True, 'message': 'Pathway deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_sister_section(request):
    try:
        data = request.data
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        sister_section = SisterSection.objects.create(
            title=data.get('title'),
            description=data.get('description')
        )
        return Response({'success': True, 'message': 'Sister section created successfully.', 'sister_section': sister_section.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_sister_section(request):
    try:
        data = request.data
        id = data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not data.get('title') or not data.get('description'):
            return Response({'success': False, 'message': 'Title and description are required.'}, status=status.HTTP_400_BAD_REQUEST)

        sister_section = SisterSection.objects.filter(id=id).first()
        if not sister_section:
            return Response({'success': False, 'message': 'Sister section not found.'}, status=status.HTTP_400_BAD_REQUEST)

        sister_section.title = data.get('title', sister_section.title)
        sister_section.description = data.get('description', sister_section.description)
        sister_section.save()
        return Response({'success': True, 'message': 'Sister section updated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_sister_section(request):
    try:
        id = request.data.get('id')
        if not id:
            return Response({'success': False, 'message': 'ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        sister_section = SisterSection.objects.filter(id=id).first()
        if not sister_section:
            return Response({'success': False, 'message': 'Sister section not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        sister_section.delete()
        return Response({'success': True, 'message': 'Sister section deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
