from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('loadings', loadings, name='loadings'),
    path('aprendiz', aprendiz, name='aprendiz'),
    path('instructor', instructor, name='instructor'),

    path('loadAprendicesMany', loadAprendicesMany, name='loadAprendicesMany'),
    path('loadInstructores', loadInstructores, name='loadInstructores'),

]
