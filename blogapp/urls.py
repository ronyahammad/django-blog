from django.urls import path
from .views import (BlogappListView,
                    BlogappPostView,
                    BlogappCreateview,
                    BlogappUpdateView,
                    BlogappDeleteView,
                    )

urlpatterns = [
    path('post/<int:pk>/delete/',BlogappDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/edit/',BlogappUpdateView.as_view(),name='post_edit'),
    path('post/new/', BlogappCreateview.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogappPostView.as_view(),name='post_detail'),
    path('',BlogappListView.as_view(),name='home'),
]