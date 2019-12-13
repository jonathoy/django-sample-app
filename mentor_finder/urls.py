from django.urls import path

from . import views

app_name = 'mentor_finder'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.CreateMentor.as_view(), name='create')
]
