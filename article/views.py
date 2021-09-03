from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Article, Comment, Image
from .forms import CommentForm
import random


def search(request):
    s = request.GET.get('q')
    tt = Article.objects.filter(Q(title__icontains=s) | Q(text__icontains=s)).order_by('-id')
    length = len(tt)
    page = request.GET.get('page', 1)
    paginator = Paginator(tt, 7)
    try:
        t = paginator.page(page)
    except PageNotAnInteger:
        t = paginator.page(1)
    except EmptyPage:
        t = paginator.page(paginator.num_pages)
    return render(request, 'search.html', {'t': t, 'length': length})


def about(request):
    return render(request, 'about.html', {})


def author(request):
    return render(request, 'author.html', {})


class ArtListView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'context'
    paginate_by = 7


class ArtDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'context'
    form_class = CommentForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        sd = self.get_object()
        if form.is_valid():
            form.save()
            messages.success(request, 'Назари шумо сабт шуд! Баъди тафтиш нашр мешавад.')
        return redirect(reverse('art-detail', kwargs={'pk': sd.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # update views
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save()
        # related articles in random order
        dg = list(Article.objects.filter(category=self.object.category.id).values('id', 'title').order_by('-id'))
        if len(dg) < 5:
            context['digar'] = random.sample(dg, len(dg))
        else:
            context['digar'] = random.sample(dg, 5)
        context['com1'] = self.form_class(initial={'article': self.object})
        context['com2'] = Comment.objects.filter(article=self.object.id).filter(active=True)
        return context


class ArtCView(ListView):
    template_name = 'category.html'
    context_object_name = 'context'
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        if self.kwargs['id']:
            queryset = Article.objects.filter(category=self.kwargs['id'])
        return queryset


class ArtTView(ListView):
    template_name = 'type.html'
    context_object_name = 'context'
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        if self.kwargs['id']:
            queryset = Article.objects.filter(type=self.kwargs['id'])
        return queryset


class ImageView(ListView):
    template_name = 'images.html'
    context_object_name = 'context'
    paginate_by = 8

    def get_queryset(self):
        queryset = Image.objects.all()
        return queryset

