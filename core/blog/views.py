from django.shortcuts import render

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Витягуємо всі пости
    return render(request, 'blog/post_list.html', {'posts': posts})
