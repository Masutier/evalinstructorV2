import os, json
import hashlib
import sqlite3 as sql3
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Aprendiz
from .utils import *
from .sendEmail import sendEmail
from .toHash import toHash


now = datetime.now()
year = now.strftime("%Y")

# Origen folder for load many files at once 
aprendiz_origen_path = "/home/gabriel/Downloads/ARRIVE/APRENDICESSS/"

# Folder to aprendiz sqlite3
Sqlite_aprendiz_destiny_path = "../evalinstructorV2/dbs/staff.db"
# Folder to save csvs apprentice
Aprendice_destiny_path = "../evalinstructorV2/csvs/laprend/"


Sqlite_instructor_destiny_path = "../evalinstructorV2/dbs/staff.db"


def loadings(request):

    context = {'title': 'Subir Listas'}
    return render(request, 'loadlist/loadings.html', context)


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

        # create hash
    dataframe = toHash(dataframe)

        # enviar los correos
    for i, row in dataframe.iterrows():
        context = ({"ficha": row['FICHA'], "first_name": row['NOMBRE'], 'last_name': row['APELLIDOS'], 'hash': row['HASH']})
        emailSubject = "Jornada de evaluacion de tus Instructores"
        sendTo = row['CORREO_ELECTRONICO']

        sendEmail(request, context, emailSubject, sendTo)
        dataframe.at[i, 'HASH_SEND'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    messages.success(request, 'Los correos se enviaron satisfactoriamente')

        # DATABASE
    conn = sql3.connect(Sqlite_aprendiz_destiny_path)
    dataframe.to_sql(name="loadings_aprendiz", con=conn, if_exists="append", index=False)
    conn.close()

        # save to csv
    dataframe.to_csv(endDir + "allAprendiz.csv", index=True)

        # delete only xls, xlsx files
    for file in os.listdir(aprendiz_origen_path):
        if file.endswith('.xls') or file.endswith('.xlsx'):
            os.remove(aprendiz_origen_path + file)

    messages.success(request, 'Las listas de los aprendices se procesaron correctamente')

    return redirect("home")


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

        if filenamex[1] == "xls" or filenamex[1] == "xlsx":
            dataframe = pd.read_excel(fileinn)
        else:
            messages.success(request, "El archivo no es valido, revise que sea .xls o .xlsx")
            return redirect("/")

            # Limpia la data
        dataframe = clean_data_instructor(dataframe)

            # create hash
        dataframe = toHash(dataframe)

        dataframe['FECHA_DEL_REPORTE'] = datetime.now()

            # save to csv
        dataframe.to_csv(endDir + "allInstructores_" + timing + ".csv", index=True)

            # DATABASE
        conn = sql3.connect(Sqlite_instructor_destiny_path)
        dataframe.to_sql(name="loadings_instructor", con=conn, if_exists="append", index=False)
        conn.close()

        messages.success(request, 'La lista de los instructores se proceso correctamente')

    return redirect("home")
