from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # Что отображать в списке всех брендов
    list_display = ('name', 'logo_preview')
    # По каким полям искать
    search_fields = ('name',)

    # Маленькая хитрость, чтобы видеть превью логотипа в админке
    def logo_preview(self, obj):
        if obj.logo:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.logo.url)
        return "Нет логотипа"
    
    logo_preview.short_description = "Логотип"