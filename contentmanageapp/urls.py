from django.urls import path
from . import views

app_name = 'contentmanageapp'

urlpatterns = [
    path('external', views.external, name='external'),
    path('internal', views.internal, name='internal'),
    path('', views.top, name='top'),
]
