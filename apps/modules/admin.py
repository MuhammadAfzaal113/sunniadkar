from django.contrib import admin
from apps.modules.models import *


@admin.register(Salawat)
class SalawatAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at',)
    fields = ('title', 'description')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(DuaCategory)
class DuaCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at')
    fields = ('category_name',)
    search_fields = ['category_name']
    list_filter = ('category_name', 'created_at')


@admin.register(Dua)
class DuaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'category')
    fields = ('title', 'description', 'category')
    search_fields = ['title', 'category']
    list_filter = ('category', 'title')


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'link')
    fields = ('title', 'description', 'link')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(Mewlid)
class MewlidAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    fields = ('title', 'description')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(Qasida)
class QasidaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    fields = ('title', 'description')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at')
    fields = ('title', 'link')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'created_at')  # Fixed typo
    fields = ('title', 'description', 'link')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(QA)
class QAAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at')
    fields = ('question', 'answer')
    search_fields = ['question']
    list_filter = ('question', 'created_at')


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at')
    fields = ('title', 'link')
    search_fields = ['title']
    list_filter = ('title', 'created_at')


@admin.register(MarriageGuide)
class MarriageGuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'created_at')
    fields = ('title', 'description', 'link')
    search_fields = ['title']
    list_filter = ('title', 'created_at')
