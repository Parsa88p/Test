from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('updateprofile/', views.user_update, name='update'),
    path('change/', views.change_password, name='change')
]