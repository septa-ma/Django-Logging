from django.urls import path
from .views import *

urlpatterns = [
    path('test/', Example_Log.as_view(), name='test'),
]