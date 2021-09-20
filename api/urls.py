from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from article import views
# from users import views as u_view
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('articles', views.ArtView, 'article')
# router.register('profiles', u_view.ProfileView, 'profile')
# router.register('users', u_view.UserView, 'user')
# router.register('types', views.TypeView, 'type')
# router.register('cats', views.CatView, 'cat')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls', namespace='article')),
    path('user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
