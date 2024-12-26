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
def get_salawat_by_id_view(request, id):
    try:
        salawat = Salawat.objects.filter(id=id).values('id', 'title', 'description').first()
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
def get_dua_category_by_id_view(request, id):
    try:
        dua_category = DuaCategory.objects.filter(id=id).values('id', 'category_name').first()
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
            pledge_salawat = PledgeSalawat.objects.filter(campaign=request.query_params.get('campaign', None)).values('campaign', 'name', 'address', 'salat').order_by('-created_at')
        else:
            pledge_salawat = PledgeSalawat.objects.values('campaign', 'name', 'address', 'salat').order_by('-created_at')
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
        campaign_obj = Campaign.objects.filter(id=data.get('campaign', None)).first()
        if not campaign_obj:
            return Response({'success': False, 'message': 'Campaign not found.'}, status=status.HTTP_400_BAD_REQUEST)
        PledgeSalawat.objects.create(
            campaign=campaign_obj,
            pledge_count=data.get('amount', None),
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
def get_campaigns_with_pledges(request):
    try:
        campaigns = Campaign.objects.all()
        response_list = []

        for campaign in campaigns:
            # Fetch all pledges related to this campaign
            pledges = PledgeSalawat.objects.filter(campaign=campaign).all()

            # Prepare campaign_pledge list
            campaign_pledge = [
                {
                    "name": pledge.name,
                    "address": pledge.address,
                    "salat": pledge.salat,
                    "created_at": pledge.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    "pledge_count": pledge.pledge_count
                }
                for pledge in pledges
            ]

            # Add campaign data to response
            response_list.append({
                "id": campaign.id,
                "name": campaign.name,
                "joined": pledges.count(),  # Count of campaign_pledge list
                "campaign_pledge": campaign_pledge
            })
        response_data = {
            'success': True,
            'message': 'Campaign fetched successfully.',
            'campaign': response_list
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"success": False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
