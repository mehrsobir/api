from .models import Article, Category, Type
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ArtSerialiser
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly


class ArticlePermission(BasePermission):
    message = "Editing restricted"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ArticleList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('title', 'text', 'author__username')


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView, ArticlePermission):
    permission_classes = [ArticlePermission]
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



