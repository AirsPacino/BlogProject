from django.shortcuts import render,get_object_or_404
import markdown
from .models import Post
from comment.forms import CommentForm

# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {
        'post_list':post
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

    form = CommentForm()
    """取出这篇文章所有的评论"""
    comment_list = post.comment_set.all()

    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }

    return render(request, 'blog/detail.html', context)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def category(request, cate_name):
    """
    这里要搞清楚Post类的category属性是什么类型。。它是一个对象而不是值
    所以要么先得到这个对象，要么调用这个对象的属性
    """
    post_list = Post.objects.filter(category__name=cate_name)
    return render(request, 'blog/index.html', context={'post_list':post_list})