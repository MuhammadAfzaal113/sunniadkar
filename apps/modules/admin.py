from django.contrib import admin

# Register your models here.

from apps.modules.models import Salawat, DuaCategory, Dua, Books


@admin.register(Salawat)
class SalawatAdmin(admin.ModelAdmin):
    list_display = ('salawat_title', 'salawat_text', 'created_at', 'created_by')
    fields = ('salawat_title', 'salawat_text')
    search_fields = ('salawat_title', 'salawat_text')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('salawat_title', 'created_at')


@admin.register(DuaCategory)
class DuaCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'created_by')
    fields = ('category_name',)
    search_fields = ('category_name',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('category_name', 'created_at')


@admin.register(Dua)
class DuaAdmin(admin.ModelAdmin):
    list_display = ('dua_title', 'dua_text', 'created_at', 'category')
    fields = ('dua_title', 'dua_text', 'category')
    search_fields = ('dua_title', 'dua_text', 'category')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('category', 'dua_title', 'created_at')


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_text', 'created_at', 'book_link')
    fields = ('book_title', 'book_text', 'book_link')
    search_fields = ('book_title', 'book_text')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('book_title', 'created_at')
