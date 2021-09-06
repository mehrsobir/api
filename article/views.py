from .models import Article, Category, Type
from rest_framework import viewsets
from .serializers import ArtSerialiser, CatSerialiser, TypeSerialiser


class ArtView(viewsets.ModelViewSet):
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()

class CatView(viewsets.ModelViewSet):
    serializer_class = CatSerialiser
    queryset = Category.objects.all()

class TypeView(viewsets.ModelViewSet):
    serializer_class = TypeSerialiser
    queryset = Type.objects.all()



