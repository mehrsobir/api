from django.urls import path, include
from .views import ArticleList, ArticleDetail, PostListDetailfilter
# from rest_framework.routers import DefaultRouter

app_name = 'api'

# router = DefaultRouter()
# router.register('', ArticleList, basename='article')
# urlpatterns = router.urls


urlpatterns = [
    path('', ArticleList.as_view(), name='listcreate'),
    path('<str:slug>/', ArticleDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),

]