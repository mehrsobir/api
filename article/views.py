from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Article, Category, Type
from .forms import CommentForm
import random
from rest_framework import status, viewsets
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
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



