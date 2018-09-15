from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import DetailView

def article_by_name(request):
    articles=Article.objects.all()
    return render(request,'slugapp/index.html', {'articles':articles})

class TaskView(DetailView):
    template_name = 'slugapp/detail.html'
    model = Article
    context_object_name = 'article'


# def article_detail(request, slug):
#     article= get_object_or_404(Article, slug= slug)
#     return render(request, 'slugapp/detail.html', {'article': article})