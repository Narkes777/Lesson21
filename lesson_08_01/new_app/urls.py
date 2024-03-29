from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),

    path('authors/', views.AuthorList.as_view(), name='author_list'),

    path('', views.MainPage.as_view(), name='main_page')
]

