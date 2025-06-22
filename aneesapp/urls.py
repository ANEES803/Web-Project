from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
     path('contact/', views.contact_view, name='contact'),
    
]
