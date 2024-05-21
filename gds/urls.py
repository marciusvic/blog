from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gds', views.gds, name='gds'),
    path('consultoria', views.consultoria, name='consultoria')
]