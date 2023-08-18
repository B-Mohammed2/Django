from django.urls import path
from . import views

urlpatterns=[
    # homepage rout
    path('home/',views.home,name='homepage'),
    # adding this empty path to open the link in home page wher run
    path('',views.home),
    path('add_charity/', views.add_charities,name='addcharity')
]