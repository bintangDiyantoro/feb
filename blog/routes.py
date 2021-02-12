from django.urls import path
from .controllers import *

app_name = 'blog'

urlpatterns = [
    path('create', Create.as_view(), name='create'),
    path('', Index.as_view(), name='index'),
    path('detail/<str:slug>', Detail.as_view(), name='detail'),
    path('edit/<str:slug>', Update.as_view(), name='edit'),
    path('delete/<str:slug>', Delete.as_view(), name='delete')
]
