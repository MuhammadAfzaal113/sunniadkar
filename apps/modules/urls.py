from django.urls import path
from .views import *

urlpatterns = [
    path('salawat', get_salawat_view, name='get_salawat_view'),
    path('salawat/<int:id>', get_salawat_by_id_view, name='get_salawat_by_id_view'),
    path('salawat/delete/<int:id>', delete_salawat_view, name='delete_salawat_view'),
    path('dua_category', get_dua_category_view, name='get_dua_category_view'),
    path('dua_category/<int:id>', get_dua_category_by_id_view, name='get_dua_category_by_id_view'),
    path('dua_category/delete/<int:id>', delete_dua_category_view, name='delete_dua_category_view'),
    path('dua_list', get_dua_view_by_category_view, name='get_dua_view_by_category_view'),
    path('get_books', get_book_view, name='get_book_view'),
    path('get_mawlid', get_mawlid_view, name='get_mawlid_view'),
]
