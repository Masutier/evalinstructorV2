import os
import csv, json
import pandas as pd
from datetime import datetime, date
from django.shortcuts import render, redirect
import sqlite3 as sql3
from .models import Instructor, Aprendiz
from .utils import *


now = datetime.now()
year = now.strftime("%Y")

# Origen folder for load many files at once 
aprendiz_origen_path = "/home/gabriel/Downloads/ARRIVE/to_load/"

# Folder to aprendiz sqlite3
Sqlite_aprendiz_destiny_path = "../evalinstructor/dbs/staff.db"
# Folder to save csvs apprentice
Aprendice_destiny_path = "../evalinstructor/csvs/laprend/"

# Folder to instructor sqlite3
Sqlite_instructor_destiny_path = "../evalinstructor/dbs/staff.db"
# Folder to save csvs instructor
instructor_destiny_path = "../evalinstructor/csvs/linstr/"


def takeFicha(elem):
    return elem[2]


def loadings(request):

    context = {'title': "Loadings"}
    return render(request, "loadings/loadings.html", context)


def aprendiz(request):
    aprendices = Aprendiz.objects.using('staff_db').all()

    cant = aprendices.count()

    context = {'title': "Aprendices", 'aprendices': aprendices, 'cant':cant}
    return render(request, "loadings/aprendiz.html", context)


def instructor(request):
    instructores = Instructor.objects.using('staff_db').all()

    cant = instructores.count()


    context = {'title': "Instructores", 'instructores': instructores, 'cant':cant}
    return render(request, "loadings/instructor.html", context)


def loadAprendicesOne(request):
    allAprendiz = []

    if request.method == "POST":
            # crear directorio si no existe
        endDir = crearAprendizFolder()

            # Recibe file y separa nombre de la extension
        fileinn = request.FILES["aprendfileinn"]
        namefile = fileinn.filename
        filenamex = namefile.split('.')

        if filenamex[1] == "csv":
            df = pd.read_csv(fileinn, index_col=False)
        elif filenamex[1] == "ods":
            df = pd.read_excel(fileinn, engine="odf")
        elif filenamex[1] == "xls" or filenamex[1] == "xlsx":
            df = pd.read_excel(fileinn)
        else:
            flash("El archivo no es valido, revise que sea .csv, .ods, .xls o .xlsx")
            return redirect("/")

            # Remove unwanted rows

            # Remove unwanted columns

            # Clean Data
        df = clean_data_aprendiz(df)

            # save to csv
        df.to_csv('../fichas_evaluacion_instructores/laprend/II_SEM_2023/aprendices.csv', index = False)

            # DATABASE
        conn = sql3.connect(Sqlite_aprendiz_destiny_path)
        df.to_sql(name="aprendiz", con=conn, if_exists="append", index=False)
        conn.close()

    return redirect("aprendiz")
    #return redirect("/")


def loadAprendicesMany(request):
    timing = datetime.now().strftime("%b_%Y")
    frames=[]
    xls_files = []
    allApren = []

    # Create directory if not exists
    endDir = crearAprendizFolder()

    # Load only xls, xlsx files
    for file in os.listdir(aprendiz_origen_path):
        if file.endswith('.xls') or file.endswith('.xlsx'):
            ficha1 = []
            ficha = ""
            lenficha = 6

            # Get ficha number
            data = pd.read_excel(io=aprendiz_origen_path + file, header=None)
            fechaReporte = data.iat[3,2]
            celx = data.iat[1,2]
            for i in celx:
                if lenficha >= 0:
                    ficha1.append(i)
                    lenficha -= 1
            ficha = ''.join(str(e) for e in ficha1)

            # Delete first 4 rows from file
            filenamex = file.split('.')
            dfx = pd.read_excel(io=aprendiz_origen_path + file, header=None)
            df1 = dfx.drop(dfx.index[0:4])
            df1.reset_index(drop=True, inplace=True)
            df1.drop(index=4)
            df1.columns = df1.iloc[0]
            df1 = df1[1:]

            # Add columns for fechaReporte and ficha
            df1['fecha_del_reporte'] = fechaReporte
            df1['ficha'] = ficha

            # Save processed sheets into one master dataframe
            allApren.append(df1)

        # Join all files in one dataframe
    dataframe = pd.concat(allApren, axis=0)
        # clean columns names and data
    dataframe = clean_data_aprendiz(dataframe)
        # save to csv
    dataframe.to_csv(endDir + "allAprendices_" + timing + ".csv", index=False, mode="a")
    
        # DATABASE
    conn = sql3.connect(Sqlite_aprendiz_destiny_path)
    dataframe.to_sql(name="loadings_aprendiz", con=conn, if_exists="append", index=False)
    conn.close()

        # delete only xls, xlsx files
    for file in os.listdir(aprendiz_origen_path):
        if file.endswith('.xls') or file.endswith('.xlsx'):
            os.remove(aprendiz_origen_path + file)

    return redirect("aprendiz")


def loadInstructores(request):
    timing = datetime.now().strftime("%b_%Y")
    allInstr = []
    if request.method == "POST":
            # crear directorio si no existe
        endDir = crearInstructorFolder()
            # Recibe file y separa nombre de la extension
        fileinn = request.FILES["instructorFileIn"]
        nameFile = fileinn.name
        filenamex = nameFile.split('.')

        if filenamex[1] == "csv":
            dataframe = pd.read_csv(fileinn, index_col=False)
        elif filenamex[1] == "xls" or filenamex[1] == "xlsx":
            dataframe = pd.read_excel(fileinn)
        elif filenamex[1] == "ods":
            dataframe = pd.read_excel(fileinn, engine="odf")
        else:
            flash("El archivo no es valido, revise que sea .csv, .xls, .xlsx o .ods")
            return redirect("/")

            # Limpia la data
        dataframe = clean_data_instructor(dataframe)

            # save to csv
        dataframe.to_csv(endDir + "allInstructores_" + timing + ".csv", index=True)

        dataframe['FECHA_DEL_REPORTE'] = datetime.now()

            # DATABASE
        conn = sql3.connect(Sqlite_instructor_destiny_path)
        dataframe.to_sql(name="loadings_instructor", con=conn, if_exists="append", index=False)
        conn.close()

    return redirect("instructor")


def file404():

    return render("partials/file404.html", title="Error")
