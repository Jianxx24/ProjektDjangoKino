from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.loginApp,name='login'),
    path('register/',views.register, name='register'),
    path('movies/', views.movies, name='movies'),
    path('shows/', views.allshows, name='allshows'),
    path('show/<str:title>/', views.shows, name='shows'),
    path('tickets/<str:title>/<str:tickets>/', views.tickets, name='tickets'),
    path('orders/', views.orderHandling, name='orders'),
    path('mytickets/', views.mytickets, name='mytickets'),

]