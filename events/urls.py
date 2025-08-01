from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    
    
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='admin_login'),
    path('admin/logout/', auth_views.LogoutView.as_view(), name='admin_logout'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # NGO 
    path('admin/ngo/create/', views.ngo_create, name='ngo_create'),
    path('admin/ngo/edit/<int:pk>/', views.ngo_edit, name='ngo_edit'),
    path('admin/ngos/', views.ngo_list, name='ngo_list'),
    
    # Event 
    path('admin/event/create/', views.event_create, name='event_create'),
    path('admin/event/edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('admin/events/', views.event_list_admin, name='event_list_admin'),
]
