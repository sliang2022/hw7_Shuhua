from django.urls import path
from blogging.views import stub_view, list_view, detail_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/stub_view', stub_view, name="stub_view"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]