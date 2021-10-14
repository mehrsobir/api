from django.urls import path, include
from .views import ArticleList, ArticleDetail, PostListDetailfilter, \
                    CreatePost, AdminPostDetail, EditPost, DeletePost, getType, getCat

app_name = 'api'

urlpatterns = [
    path('', ArticleList.as_view(), name='listpost'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='detailarticle'),
    path('search/', PostListDetailfilter.as_view(), name='searcharticle'),
    path('type/', getType.as_view(), name='gettypecat'),
    path('cat/', getCat.as_view(), name='gettypecat'),
    # Post Admin URLs
    path('admi/create/', CreatePost.as_view(), name='createpost'),
    path('admi/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admi/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admi/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),

]
