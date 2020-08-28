from django.shortcuts import render

from .models import Article
from django.views.generic import ListView, DetailView


class ArticleList(ListView):
    model = Article
    queryset = Article.objects.all()
    context_object_name = 'articles'
    template_name = 'blog/list.html'
    
class ArticleDetail(DetailView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'

