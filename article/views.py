from .models import Article, Category, Type
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ArtSerialiser
from rest_framework.permissions import AllowAny, SAFE_METHODS, BasePermission, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ArticlePermission(BasePermission):
    message = "Editing restricted"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ArticleList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtSerialiser

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Article, slug=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Article.objects.all()



# class ArticleList(viewsets.ViewSet):
#     permission_classes = [AllowAny]
#     queryset = Article.postobjects.all()
#
#     def list(self, request):
#         serializer_class = ArtSerialiser(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = ArtSerialiser(post)
#         return Response(serializer_class.data)



# class ArticleList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Article.objects.all()
#     serializer_class = ArtSerialiser
#     filter_backends = (SearchFilter, OrderingFilter,)
#     search_fields = ('title', 'text', 'author__username')
#
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView, ArticlePermission):
#     permission_classes = [ArticlePermission]
#     queryset = Article.objects.all()
#     serializer_class = ArtSerialiser




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



