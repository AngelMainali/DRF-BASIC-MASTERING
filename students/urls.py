from django.urls import path
from . import views

urlpatterns = [
    #web application endpoints
    path('', views.students, name='students'),

    
]
