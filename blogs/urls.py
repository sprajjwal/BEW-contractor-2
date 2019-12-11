from django.shortcuts import render
from django.urls import path
from blogs.views import PageListView, PageDetailView, PageNew, BlogUpdate, delete_object


urlpatterns = [
    path('', PageListView.as_view(), name='blog-list-page'),
    path('submit/', PageNew.as_view(), name="submit-blog"),
    path('<str:slug>/update', BlogUpdate.as_view(), name='blog-update-page'),
    path('<str:slug>/delete', delete_object, name='blog-delete-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='blog-details-page'),
    
]
