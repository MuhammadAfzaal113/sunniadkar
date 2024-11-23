from django.contrib import admin

# Register your models here.

from apps.salawat.models import Salawat


@admin.register(Salawat)
class SalawatAdmin(admin.ModelAdmin):
    list_display = ('salawat_title', 'salawat_text', 'created_at', 'updated_at')
    search_fields = ('salawat_title', 'salawat_text')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('salawat_title', 'created_at')

