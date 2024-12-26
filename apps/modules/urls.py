from django.urls import path
from .views import *

urlpatterns = [
    path('salawat', get_salawat_view, name='get_salawat_view'),
    path('salawat/<str:id>', get_salawat_by_id_view, name='get_salawat_by_id_view'),
    path('salawat/delete/<str:id>', delete_salawat_view, name='delete_salawat_view'),
    path('dua-category', get_dua_category_view, name='get_dua_category_view'),
    path('dua-category/<str:id>', get_dua_category_by_id_view, name='get_dua_category_by_id_view'),
    path('dua-category/delete/<str:id>', delete_dua_category_view, name='delete_dua_category_view'),
    path('dua-list', get_dua_view_by_category_view, name='get_dua_view_by_category_view'),
    path('books', get_book_view, name='get_book_view'),

    path('get-mewlid', get_mewlid, name='get_mewlid'),
    path('get-qasida', get_qasida, name='get_qasida'),
    path('get-lecture', get_lecture, name='get-lecture'),
    path('get-article', get_article, name='get_article'),
    path('get-QA', get_qa, name='get_QA'),
    path('get-download', get_download, name='get_download'),
    path('get-marriage-guide', get_marriage_guide, name='get_marriage_guide'),
    path('get-pledge-salawat', get_pledge_salawat, name='get_pledge_salawat'),
    path('create-pledge-salawat', create_pledge_salawat, name='create_pledge_salawat'),
    path('get-LifeLesson', get_LifeLesson, name='get_LifeLesson'),
    path('create-community', create_community, name='create_community'),
    path('get-community-category', get_community_category, name='get_community_category'),
    
    path('community', get_community, name='get_community'),
    path('like-post', like_post, name='like_post'),
    path('dua-post', dua_post, name='dua_post'),
    path('ameen-post', ameen_post, name='ameen_post'),
    
    path('get-campaign', get_campaign_list, name='get_campaign_list'),
    path('get-mentality-booster', get_mentality_booster, name='get_mentality_booster'),
    path('get-health-tips', get_health_tips, name='get_health_tips'),
    

# -------------------- Admin Panel --------------------
    # Salawat URLs
    path('salawat/create', create_salawat, name='create_salawat'),
    path('salawat/update', update_salawat, name='update_salawat'),
    path('salawat/delete', delete_salawat, name='delete_salawat'),

    # DuaCategory URLs
    path('duacategory/create', create_dua_category, name='create_dua_category'),
    path('duacategory/update', update_dua_category, name='update_dua_category'),
    path('duacategory/delete', delete_dua_category, name='delete_dua_category'),

    # Dua URLs
    path('dua/create', create_dua, name='create_dua'),
    path('dua/update', update_dua, name='update_dua'),
    path('dua/delete', delete_dua, name='delete_dua'),

    # Books URLs
    path('books/create', create_book, name='create_books'),
    path('books/update', update_book, name='update_books'),
    path('books/delete', delete_book, name='delete_books'),

    # Mewlid URLs
    path('mewlid/create', create_mewlid, name='create_mewlid'),
    path('mewlid/update', update_mewlid, name='update_mewlid'),
    path('mewlid/delete', delete_mewlid, name='delete_mewlid'),

    # Qasida URLs
    path('qasida/create', create_qasida, name='create_qasida'),
    path('qasida/update', update_qasida, name='update_qasida'),
    path('qasida/delete', delete_qasida, name='delete_qasida'),

    # Lecture URLs
    path('lecture/create', create_lecture, name='create_lecture'),
    path('lecture/update', update_lecture, name='update_lecture'),
    path('lecture/delete', delete_lecture, name='delete_lecture'),

    # Article URLs
    path('article/create', create_article, name='create_article'),
    path('article/update', update_article, name='update_article'),
    path('article/delete', delete_article, name='delete_article'),

    # QA URLs
    path('qa/create', create_qa, name='create_qa'),
    path('qa/update', update_qa, name='update_qa'),
    path('qa/delete', delete_qa, name='delete_qa'),

    # Download URLs
    path('download/create', create_download, name='create_download'),
    path('download/update', update_download, name='update_download'),
    path('download/delete', delete_download, name='delete_download'),

    # MarriageGuide URLs
    path('marriageguide/create', create_marriage_guide, name='create_marriage_guide'),
    path('marriageguide/update', update_marriage_guide, name='update_marriage_guide'),
    path('marriageguide/delete', delete_marriage_guide, name='delete_marriage_guide'),

    # LifeLesson URLs
    path('lifelesson/create', create_life_lesson, name='create_life_lesson'),
    path('lifelesson/update', update_life_lesson, name='update_life_lesson'),
    path('lifelesson/delete', delete_life_lesson, name='delete_life_lesson'),

    # Campaign URLs
    path('campaign/create', create_campaign, name='create_campaign'),
    path('campaign/update', update_campaign, name='update_campaign'),
    path('campaign/delete', delete_campaign, name='delete_campaign'),

    # CommunityCategory URLs
    path('communitycategory/create', create_community_category, name='create_community_category'),
    path('communitycategory/update', update_community_category, name='update_community_category'),
    path('communitycategory/delete', delete_community_category, name='delete_community_category'),

    # MentalityBooster URLs
    path('mentalitybooster/create', create_mentality_booster, name='create_mentality_booster'),
    path('mentalitybooster/update', update_mentality_booster, name='update_mentality_booster'),
    path('mentalitybooster/delete', delete_mentality_booster, name='delete_mentality_booster'),

    # HealthTips URLs
    path('healthtips/create', create_health_tips, name='create_health_tips'),
    path('healthtips/update', update_health_tips, name='update_health_tips'),
    path('healthtips/delete', delete_health_tips, name='delete_health_tips'),
    
]
