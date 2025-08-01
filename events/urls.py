from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),

    # Admin/Auth Views
    path('dashboard/login/', auth_views.LoginView.as_view(
        template_name='admin/login.html',
        next_page='admin_dashboard'  # 👈 add this line
    ), name='admin_login'),

    path('dashboard/logout/', auth_views.LogoutView.as_view(), name='admin_logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # NGO URLs
    path('dashboard/ngo/create/', views.ngo_create, name='ngo_create'),
    path('dashboard/ngo/edit/<int:pk>/', views.ngo_edit, name='ngo_edit'),
    path('dashboard/ngos/', views.ngo_list, name='ngo_list'),

    # Event URLs
    path('dashboard/event/create/', views.event_create, name='event_create'),
    path('dashboard/event/edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('dashboard/events/', views.event_list_admin, name='event_list_admin'),
]

