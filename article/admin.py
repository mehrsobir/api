from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Type)


@admin.register(Article)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'type', 'category', 'pubdate')
    list_filter = ['author', 'category', 'type', 'pubdate']
    prepopulated_fields = {'slug': ('title',)}

