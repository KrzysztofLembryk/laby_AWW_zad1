from django.urls import path
from . import views

app_name = "obrazki_app"
urlpatterns = [ 
    path('', views.index, name='index'),
    path('login/', views.login_ArtUser, name='login'),
    path('logout/', views.logout_view, name='logout'),
]