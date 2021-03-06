from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<slug>/', views.PostDetailView.as_view(), name='post-detail'),
]
