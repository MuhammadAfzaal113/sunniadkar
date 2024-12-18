from django.contrib import admin
from apps.modules.models import *


admin.site.site_header = "SunniAdkar Admin Panel"
admin.site.site_title = "SunniAdkar Admin"
admin.site.index_title = "Welcome to SunniAdkar Admin Panel"


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
    
@admin.register(LifeLesson)
class LifeLessonAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'created_at')
    fields = ('author', 'description')
    search_fields = ['author']
    list_filter = ('author', 'created_at')
    
    def get_author(self, obj):
        return str(obj.author.full_name)  
    
@admin.register(CommunityCategory)
class CommunityCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at')
    fields = ('category_name',)
    search_fields = ['category_name']
    list_filter = ('category_name', 'created_at')
    

@admin.register(Campaign)
class campaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    fields = ('name',)
    search_fields = ['name']
    list_filter = ('name', 'created_at')