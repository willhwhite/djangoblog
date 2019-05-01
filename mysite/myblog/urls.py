from django.urls import path, include
from .views import stub_view
from .views import list_view, detail_view
from .feeds import LatestEntriesFeed


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('latest/feed/', LatestEntriesFeed()),
]
