import os
import csv, json
import pandas as pd
import sqlite3 as sql3
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
        if request.method == 'POST':
            ficha = request.POST.get('ficha')
            documento = request.POST.get('documento')
            
            request.session['ficha'] = ficha
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
            
            #     # Buscar Tests
            # try:
            #     testings = Testings.objects.using('testings_db').all()
            #     for instr in allinstructores:
            #         if instr in testings:
            #             print('*********** testings', instr)
            # finally:
            #     pass

            request.session['instructoresMuchos'] = allinstructores
            instructoresMuchos = request.session['instructoresMuchos']

            context = {'title': "Escoge el Instructor", 'aprendix':aprendix, 'instructores':instructores}
            return render(request, "testings/pickInst.html", context)

    
    else:
        print('start 33')
        instructores = []
        ficha = request.session['ficha']
        documento = request.session['aprendiz']
        instructoresMuchos = request.session['instructoresMuchos']

            # Buscar instructores
        instructorex = Instructor.objects.using('staff_db').filter(FICHA = ficha)
        
        for instruc in instructorex:
            if instruc.NUMERO_DE_DOCUMENTO in instructoresMuchos:
                instructores.append(instruc)

            # Buscar aprendices
        aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = documento)


        context = {'title': "Escoge el Instructor", 'aprendix':aprendix, 'instructores':instructores}
        return render(request, "testings/pickInst.html", context)

    return redirect("home")


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

            context = {'title': "Eveluación Instructor", 'aprendix':aprendix, 'instructor':instructor}
            return render(request, "testings/testing.html", context)

    else:
        aprendiz = request.session['aprendiz']
        ininstructor = request.POST.get('instructor')

            # Buscar aprendices
        aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = aprendiz)
            # Buscar instructores
        instructor = Instructor.objects.using('staff_db').get(id = ininstructor)
        request.session['instructor'] = instructor.NUMERO_DE_DOCUMENTO

    context = {'title': "Eveluación Instructor", 'aprendix':aprendix, 'instructor':instructor}
    return render(request, "testings/testing.html", context)


def saveTest(request):

    if request.method == 'POST':

        testing = request.POST
        print(testing)

            # save to csv
        newDir = semestre()
        #testing.to_csv(testing_destiny_path + newDir + 'testings.csv', index = False)

            # DATABASE
        # conn = sql3.connect(Sqlite_testing_destiny_path)
        # testing.to_sql(name="testings", con=conn, if_exists="append", index=False)
        # conn.close()
        testing.save()

        instructor = request.session['instructor']

        instructoresMuchos = request.session['instructoresMuchos']
        instructoresMuchos.remove(instructor)
        request.session['instructoresMuchos'] = instructoresMuchos
        request.session['instructor'] = ''

        instructoresMuchos = request.session['instructoresMuchos'] 
        print('instructoresMuchos', len(instructoresMuchos))

        if len(instructoresMuchos) == 0:
            messages.error(request, f"Gracias por tu participación")
            return redirect("home")

    return redirect("pickInst")

