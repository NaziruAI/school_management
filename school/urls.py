from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('school/', views.SchoolListView.as_view(), name='school-list'),
    path('school/<int:pk>/', views.SchoolDetailView.as_view(), name='school-detail'),
    path('sections/', views.SectionListView.as_view(), name='section-list'),
    path('section/<int:pk>/', views.SectionDetailView.as_view(), name='section-detail'),
    path('classes/', views.ClassListView.as_view(), name='class-list'),
    path('class/<int:pk>/', views.ClassDetailView.as_view(), name='class-detail'),
]
