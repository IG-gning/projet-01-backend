from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'prix', 'adresse', 'created_at')
    list_filter = ('ville',)
    search_fields = ('nom', 'ville', 'adresse')
