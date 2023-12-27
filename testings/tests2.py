import os
import csv, json
import pandas as pd
from datetime import datetime, date
from django.shortcuts import render, redirect
from django.contrib import messages
from loadings.models import *
from loadings.utils import semestre
from .models import Testings


# Folder to testing instructors sqlite3
Sqlite_testing_destiny_path = "../evalinstructor/dbs/testings.db"

# Folder to save csvs instructor
testing_destiny_path = "../evalinstructor/csvs/testing/"


def pickInst(request):
    aprendix = []
    allinstructores = []

    instructoresMuchos = request.session['instructoresMuchos'] 

    if len(instructoresMuchos) == 0:
        print('start')

        if request.method == 'POST':
            ficha = request.POST.get('ficha')
            request.session['ficha'] = ficha
            documento = request.POST.get('documento')
            request.session['aprendiz'] = documento

            try:
                # Buscar aprendices
                aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = documento)
            except:
                messages.error(request, f"El numero de documento no esta registrado, intente de nuevo")
                return redirect("home")

            # Buscar instructores
            instructores = Instructor.objects.using('staff_db').filter(FICHA = ficha)
            allinstructores = [i.NUMERO_DE_DOCUMENTO for i in instructores]

            if not instructores:
                messages.error(request, f"El numero de ficha no esta registrado, intente de nuevo")
                return redirect("home")

            request.session['instructoresMuchos'] = allinstructores
            instructoresMuchos = request.session['instructoresMuchos'] 

            print('start 22')
            context = {'title': "Escoge el Instructor", 'aprendix':aprendix, 'instructores':instructores}
            return render(request, "testings/pickInst.html", context)

    
    else:
        ficha = request.session['ficha']
        documento = request.session['aprendiz']
        instructores = request.session['instructoresMuchos']

        # Buscar aprendices
        aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = documento)


        context = {'title': "Escoge el Instructor", 'aprendix':aprendix, 'instructores':instructores}
        return render(request, "testings/pickInst.html", context)


def testing(request):

    instructoresMuchos = request.session['instructoresMuchos'] 

    if len(instructoresMuchos) != 0:

        if request.method == 'POST':
            aprendiz = request.session['aprendiz']
            ininstructor = request.POST.get('instructor')
            
            # Buscar aprendices
            aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = aprendiz)
            # Buscar instructores
            instructor = Instructor.objects.using('staff_db').get(id = ininstructor)
            request.session['instructor'] = instructor.NUMERO_DE_DOCUMENTO

            print('yyyyyy instructor', request.session['instructor'])

            context = {'title': "Eveluación Instructor", 'aprendix':aprendix, 'instructor':instructor}
            return render(request, "testings/testing.html", context)

    else:
        
        aprendiz = request.session['aprendiz']

        # Buscar aprendices
        aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = aprendiz)
        # Buscar instructores
        instructor = Instructor.objects.using('staff_db').get(id = ininstructor)
        request.session['instructor'] = instructor.NUMERO_DE_DOCUMENTO

        print('yyyyyy instructor', request.session['instructor'])

        context = {'title': "Eveluación Instructor", 'aprendix':aprendix, 'instructor':instructor}
        return render(request, "testings/testing.html", context)


    return redirect("home")


def saveTest(request):

    if request.method == 'POST':

        testing = request.POST
        print(testing)

            # save to csv
        newDir = semestre()
        #df.to_csv(testing_destiny_path + newDir + 'testings.csv', index = False)

            # DATABASE
        # conn = sql3.connect(Sqlite_testing_destiny_path)
        # df.to_sql(name="testings", con=conn, if_exists="append", index=False)
        # conn.close()

        instructor = request.session['instructor']
        print('xxxx instructor', instructor)
        instructoresMuchos = request.session['instructoresMuchos'] #.remove(instructor)
        print('xxxx instructoresMuchos', instructoresMuchos)
        #request.session['instructor'] = ''

        instructoresMuchos = request.session['instructoresMuchos'] 
        print('instructoresMuchos', len(instructoresMuchos))

    return redirect("testing")

