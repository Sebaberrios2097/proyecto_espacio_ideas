from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fono', 'insta')
    search_fields = ('user__username', 'fono', 'insta')
    list_filter = ('user__username', 'fono', 'insta')
    fieldsets = (
        ('Información del usuario', {
            'fields': ('user',)
        }),
        ('Información adicional', {
            'fields': ('fono', 'insta')
        }))

admin.site.register(Profile)