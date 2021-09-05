from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'affiliation',)



