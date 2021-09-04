from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Type)


@admin.register(Article)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'category', 'pubdate', 'views')
    list_filter = ['category', 'type', 'pubdate']

