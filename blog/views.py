from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown

# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'post_list': post_list,
    }

    return render(request, 'blog/index.html', context)

def detail(request, id):
    """取出主键pk值为id的对象，否则报404"""
    post = get_object_or_404(Post, pk=id)

    """这里最好不要改，还不太懂，对body进行渲染"""
    post.body = markdown.markdown(post.body, extensions=[
                                   'markdown.extensions.extra',
                                   'markdown.extensions.codehilite',
                                   'markdown.extensions.toc'
                                 ])

    return render(request, 'blog/detail.html', context={'post': post})
