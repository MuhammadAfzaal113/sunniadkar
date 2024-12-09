from django.urls import path
from .views import *

urlpatterns = [
    path('get-salawat', get_salawat_view, name='get_salawat_view'),
    path('salawat/<str:id>', get_salawat_by_id_view, name='get_salawat_by_id_view'),
    path('salawat/delete/<str:id>', delete_salawat_view, name='delete_salawat_view'),
    path('get-dua-category', get_dua_category_view, name='get_dua_category_view'),
    path('get-dua-category/<str:id>', get_dua_category_by_id_view, name='get_dua_category_by_id_view'),
    path('dua-category/delete/<str:id>', delete_dua_category_view, name='delete_dua_category_view'),
    path('dua-list', get_dua_view_by_category_view, name='get_dua_view_by_category_view'),
    path('get-books', get_book_view, name='get_book_view'),

    path('get-mewlid', get_mewlid, name='get_mewlid'),
    path('get-qasida', get_qasida, name='get_qasida'),
    path('get-lecture', get_lecture, name='get-lecture'),
    path('get-article', get_article, name='get_article'),
    path('get-QA', get_qa, name='get_QA'),
    path('get-download', get_download, name='get_download'),
    path('get-marriage-guide', get_marriage_guide, name='get_marriage_guide'),
    path('get-pledge-salawat', get_pledge_salawat, name='get_pledge_salawat'),
    path('get-LifeLesson', get_LifeLesson, name='get_LifeLesson'),
    path('create-community', create_community, name='create_community'),
    
    path('get-community', get_community, name='get_community'),
    path('like-post', like_post, name='like_post'),
    path('dua-post', dua_post, name='dua_post'),
    path('ameen-post', ameen_post, name='ameen_post'),

]
