from django.urls import path, include
from .views import csrf, ArticleList, ArticleDetail, PostListDetailfilter, CreatePost, AdminPostDetail, EditPost, DeletePost
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.routers import DefaultRouter

app_name = 'api'

# router = DefaultRouter()
# router.register('', ArticleList, basename='article')
# urlpatterns = router.urls


urlpatterns = [
    path('', ArticleList.as_view(), name='listpost'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='detailarticle'),
    path('search/', PostListDetailfilter.as_view(), name='searcharticle'),
    # Post Admin URLs
    path('admi/create/', CreatePost.as_view(), name='createpost'),
    path('admi/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admi/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admi/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
    path('csrf/', csrf),
]