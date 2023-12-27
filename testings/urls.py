from django.urls import path, include
from .views import *


urlpatterns = [
    path('pickInst', pickInst, name='pickInst'),
    path('testing', testing, name='testing'),
    path('saveTest', saveTest, name='saveTest'),

]
