from django.urls import path, include
from .views import ArticleList, ArticleDetail, PostListDetailfilter, CreatePost, AdminPostDetail, EditPost, DeletePost

# from rest_framework.routers import DefaultRouter

app_name = 'api'

# router = DefaultRouter()
# router.register('', ArticleList, basename='article')
# urlpatterns = router.urls


urlpatterns = [
    path('posts/', ArticleList.as_view(), name='listcreate'),
    path('posts/<str:slug>/', ArticleDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]