from django.urls import path

from . import views

"""视图函数命名空间"""
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.detail, name='detail')
]