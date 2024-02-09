from django.urls import path
from . import views
app_name = 'plan'
urlpatterns = [
    path('Saturday/', views.Saturday,name='Saturday'),
    path('Sunday/', views.Sunday,name='Sunday'),
    path('Monday/', views.Monday,name='Monday'),
    path('Tuesday/', views.Tuesday,name='Tuesday'),
    path('Wednesday/', views.Wednesday,name='Wednesday'),
]