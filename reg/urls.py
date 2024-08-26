from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.stud_list, name='students'),
    path('create/', views.stud_create, name='stud_create'),
    path('update/<int:pk>/', views.stud_update, name='stud_update'),
    path('delete/<int:pk>/', views.stud_delete, name='stud_delete'),

    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
