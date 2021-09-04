from django.contrib import admin
from django.urls import path, include
from article import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', views.ArtView, 'article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
