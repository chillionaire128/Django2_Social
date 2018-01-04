from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('/', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<slug:name>', views.SignleGroup.as_view(), name='single'),
]
