from django.urls import path, include
from .views import *


urlpatterns = [
    path('loadings', loadings, name='loadings'),

    path('loadAprendicesMany', loadAprendicesMany, name='loadAprendicesMany'),
    path('loadInstructores', loadInstructores, name='loadInstructores'),

]

