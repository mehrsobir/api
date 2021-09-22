from django.urls import path, include
from .views import ArticleList
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('', ArticleList, basename='article')
urlpatterns = router.urls


# urlpatterns = [
#     path('', ArticleList.as_view(), name='listcreate'),
#     path('<int:pk>/', ArticleDetail.as_view(), name='detailcreate'),
#
# ]