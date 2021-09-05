from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from article import views
from users import views as u_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', views.ArtView, 'article')
router.register('profiles', u_view.ProfileView, 'profile')
router.register('users', u_view.UserView, 'user')
router.register('types', views.TypeView, 'type')
router.register('cats', views.CatView, 'cat')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
