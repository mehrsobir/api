from django.urls import path
from .views import ArtListView, search

urlpatterns = [
    path('', ArtListView.as_view(), name='articles'),
    # path('article/<int:pk>', ArtDetailView.as_view(), name='art-detail'),
    # path('category/<int:id>', ArtCView.as_view(), name='category'),
    # path('type/<int:id>', ArtTView.as_view(), name='type'),
    path('search/', search, name='search'),

]