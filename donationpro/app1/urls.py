from django.urls import path
from . import views

urlpatterns=[
    # homepage rout
    path('home/',views.home,name='homepage'),
    # adding this empty path to open the link in home page wher run
    path('',views.home),
    # Path for add charity webpage
    path('add_charity/', views.add_charities,name='addcharity'),
    # path for thank you page
    path('thank_you/', views.thank_you,name='successful')
    
]