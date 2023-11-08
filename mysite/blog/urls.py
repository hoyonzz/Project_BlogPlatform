from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_main, name='blog_main'),
    path('write/', views.blog_write, name='blog_write'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('<int:pk>/comment/', views.comment_write, name='comment_write'),
    path('<int:pk>/comment/<int:comment_pk>/edit', views.comment_edit, name='comment_edit'),
    path('category/<slug:slug>/', views.category_page, name='category_page'),
    path('search/', views.search, name='search'),
]

