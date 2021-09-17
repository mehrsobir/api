from django.urls import path, include
from .views import ArticleList, ArticleDetail

app_name = 'blog_api'

urlpatterns = [
    path('', ArticleList.as_view(), name='listcreate'),
    path('<int:pk>/', ArticleDetail.as_view(), name='detailcreate'),

]