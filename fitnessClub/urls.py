from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',views.index, name='index'),
    path('members/',views.members, name='members'),
    path('updateMembers/<int:pk>/',views.updateMembers, name='updateMembers'),
    path('membersDetailView/<int:pk>/', views.membersDetailView, name='membersDetailView'),
    
    path('packages/',views.packages, name='packages'),
    path('updatePackages/<int:pk>/',views.updatePackages, name='updatePackages'),

    path('plans/',views.plans, name='plans'),
    path('updatePlans/<int:pk>/',views.updatePlans, name='updatePlans'),

    path('trainers/',views.trainers, name='trainers'),
    path('updateTrainers/<int:pk>/',views.updateTrainers, name='updateTrainers'),
    path('trainerDetailView/<int:pk>/', views.trainerDetailView, name='trainerDetailView'),

    path('deleteMembers/<int:pk>/',views.deleteMembers, name='deleteMembers'),
    path('deletePlans/<int:pk>/',views.deletePlans, name='deletePlans'),
    path('deletePackages/<int:pk>/',views.deletePackages, name='deletePackages'),
    path('deleteTrainers/<int:pk>/',views.deleteTrainers, name='deleteTrainers'),

    path('',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.register, name='register'),   

    path('membershipvalidation/',views.membershipvalidation, name='membershipvalidation'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_complete_.html'), name='password_reset_complete'),   
]