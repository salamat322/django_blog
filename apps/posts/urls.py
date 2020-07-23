from django.urls import path

from . import views
from .feeds import LatestPostsFeed


urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post-list-tag'),
#     path('', views.PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post-detail'),
    path('<int:post_id>/share/', views.post_share, name='post-share'),
    path('feed/', LatestPostsFeed(), name='post-feed'),
]