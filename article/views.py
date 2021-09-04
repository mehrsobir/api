from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Article, Comment
from .forms import CommentForm
import random
from rest_framework import status, viewsets
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArtSerialiser



# def search(request):
#     s = request.GET.get('q')
#     tt = Article.objects.filter(Q(title__icontains=s) | Q(text__icontains=s)).order_by('-id')
#     length = len(tt)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(tt, 7)
#     try:
#         t = paginator.page(page)
#     except PageNotAnInteger:
#         t = paginator.page(1)
#     except EmptyPage:
#         t = paginator.page(paginator.num_pages)
#     return render(request, 'search.html', {'t': t, 'length': length})


# class ArtListView(APIView):
#
#     def get(self, request):
#         art = Article.objects.all()
#         serializer = ArtSerialiser(art, many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass

class ArtView(viewsets.ModelViewSet):
    serializer_class = ArtSerialiser
    queryset = Article.objects.all()



