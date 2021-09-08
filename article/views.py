from .models import Article, Category, Type
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ArtSerialiser


class PostList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser




# class ArtView(viewsets.ModelViewSet):
#     serializer_class = ArtSerialiser
#     queryset = Article.objects.all()
#     filter_backends = (SearchFilter, OrderingFilter,)
#     search_fields = ('title', 'text', 'author__username')
#
# class CatView(viewsets.ModelViewSet):
#     serializer_class = CatSerialiser
#     queryset = Category.objects.all()
#
# class TypeView(viewsets.ModelViewSet):
#     serializer_class = TypeSerialiser
#     queryset = Type.objects.all()



