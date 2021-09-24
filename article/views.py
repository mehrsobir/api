from .models import Article, Category, Type
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ArtSerialiser
from rest_framework.permissions import AllowAny, SAFE_METHODS, BasePermission, IsAuthenticated
from django.shortcuts import get_object_or_404

class ArticlePermission(BasePermission):
    message = "Editing restricted"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ArticleList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()
#
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Article, slug=item)
#
#     # Define Custom Queryset
#     def get_queryset(self):
#         # return Article.objects.all()
#         user = self.request.user
#         return Article.objects.filter(author=user)

class PostListDetailfilter(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArtSerialiser
    filter_backends = (filters.SearchFilter,)
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']


class ArticleDetail(generics.RetrieveAPIView):

    serializer_class = ArtSerialiser

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=item)


class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()



