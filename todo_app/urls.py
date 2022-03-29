from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('todo', todolistapp, name='todo'),
    path('delete_item/<str:pk>', delete_item)
]