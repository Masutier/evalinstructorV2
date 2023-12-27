from django.db import models
from django.forms import ModelForm
from django import forms
from loadings.models import *


class AprendizInfoForm(ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['FICHA', 'NOMBRE', 'APELLIDOS', 'TIPO_DE_DOCUMENTO', 'NUMERO_DE_DOCUMENTO']
