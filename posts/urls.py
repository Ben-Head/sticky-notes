from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete, register, user_login, my_posts
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', post_list, name='post_list'),  # Default view
    path('my-posts/', my_posts, name='my_posts'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': 'post_list'}, name='logout'),
]
