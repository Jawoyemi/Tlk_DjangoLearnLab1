from django.urls import path
from blog.views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(template_name='post_list.html'), name='post-list'),
    path('post/new/', PostCreateView.as_view(template_name='post_form.html'), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='post_detail.html'), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(template_name='post_form.html'), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post-delete'),
]

