from django.contrib import admin
from .models import UserExtra

class UserExtraAdmin(admin.ModelAdmin):
    list_display = ('user', 'fono', 'direccion')
    search_fields = ('user__username', 'fono', 'direccion')
    list_filter = ('user__username', 'fono', 'direccion')
    fieldsets = (
        ('Información del usuario', {
            'fields': ('user',)
        }),
        ('Información adicional', {
            'fields': ('fono', 'direccion')
        }))

admin.site.register(UserExtra, UserExtraAdmin)