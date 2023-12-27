from django.contrib import messages
from django.shortcuts import render, redirect
import sqlite3 as sql3
from .forms import AprendizInfoForm
from loadings.models import *


# Folder to aprendiz sqlite3
Sqlite_aprendiz_destiny_path = "../evalinstructor/dbs/staff.db"


def home (request):
    form = AprendizInfoForm()
    request.session['instructoresMuchos'] = ''

    context={"title": "Home", "form":form}
    return render(request, 'evalinstructor/home.html', context)

