from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArtSerialiser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.filters import SearchFilter




class ArticleList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()


class ArticleDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ArtSerialiser

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Article, id=item)


class PostListDetailfilter(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser
    filter_backends = [SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['title', 'annotation']




class CreatePost(APIView):
    permission_classes = [AllowAny]
    serializer_class = ArtSerialiser
    def post(self, request, format=None):
        serializer = ArtSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArtSerialiser


class EditPost(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()




class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()

    
