import os
import csv, json
import numpy as np
import pandas as pd
from datetime import datetime, date

# evaluacion
with open("/home/gabriel/prog/json_config/instructores.json") as config_file:
    sec_config = json.load(config_file)

# Folder to save csvs apprentice
Aprendice_destiny_path = "../evalinstructor/csvs/laprend/"

# Folder to save csvs apprentice
instructor_destiny_path = "../evalinstructor/csvs/linstr/"


def semestre():
    now = datetime.now()
    year = now.strftime("%Y")

    if int(now.strftime("%m")) < 6:
        newDir = "I_SEM_" + year + "/"
    else:
        newDir = "II_SEM_" + year + "/"

    return newDir


# Create df with csv files
def csvFiles(endDir):
    csv_files = []
    for file in os.listdir(endDir):
        if file.endswith('.csv'):
            csv_files.append(file)
    df = {}
    for file in csv_files:
        try:
            df[file] = pd.read_csv(endDir + file)
        except:
            df[file] = pd.read_csv(endDir + file, encoding = "ISO-8859-1")

    return csv_files, df


# crear Aprendice directorio si no existe
def crearAprendizFolder():
    newDir = semestre()
    try:
        os.makedirs(Aprendice_destiny_path + newDir)
        endDir = Aprendice_destiny_path + newDir
        return endDir
    except:
        if os.listdir(Aprendice_destiny_path + newDir):
            endDir = Aprendice_destiny_path + newDir
            return endDir


# crear instructor directorio si no existe
def crearInstructorFolder():
    newDir = semestre()
    try:
        os.makedirs(instructor_destiny_path + newDir)
        endDir = instructor_destiny_path + newDir
        return endDir
    except:
        endDir = instructor_destiny_path + newDir
        return endDir


# Clean file name
def clean_tbl_name(csvf):
    CleanName = csvf.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","") \
        .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N") \
        .replace("á","A").replace("é","E").replace("í","I").replace("ó","O").replace("ú","U").replace("ñ","N") \
        .replace("@","").replace("#","").replace(r"/","_").replace("\\","_").replace(r"(","").replace(")","")
    tbl_name = '{0}'.format(CleanName.split('.')[0])

    return tbl_name


def clean_data_aprendiz(dataframe):
    dataframe.columns = [x.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","").replace(".","") \
        .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N") \
        .replace("á","A").replace("é","E").replace("í","I").replace("ó","O").replace("ú","U").replace("ñ","N") \
        .replace("@","").replace("#","").replace(r"/","").replace("\\","").replace(r"(","") \
        .replace(")","") for x in dataframe.columns]

    # CLEAN DATA
    dataframe['FICHA'] = dataframe['FICHA'].astype(str)
    dataframe['FICHA'] = [x.replace(".0","") for x in dataframe['FICHA']]

    dataframe['NUMERO_DE_DOCUMENTO'] = dataframe['NUMERO_DE_DOCUMENTO'].astype(str)
    dataframe['NUMERO_DE_DOCUMENTO'] = dataframe['NUMERO_DE_DOCUMENTO'].fillna('ND')

    dataframe['CELULAR'] = dataframe['CELULAR'].astype(str)
    dataframe['CELULAR'] = dataframe['CELULAR'].fillna('ND')
    dataframe['CELULAR'] = dataframe['CELULAR'].str.replace('.0', '')

    dataframe['CORREO_ELECTRONICO'] = dataframe['CORREO_ELECTRONICO'].fillna('ND')

    dataframe['ESTADO'] = dataframe['ESTADO'].fillna('ND')

    return dataframe


    # Clean columns names
def clean_data_instructor(dataframe):

    dataframe.columns = [x.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","").replace(".","") \
        .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N") \
        .replace("á","A").replace("é","E").replace("í","I").replace("ó","O").replace("ú","U").replace("ñ","N") \
        .replace("@","").replace("#","").replace(r"/","").replace("\\","").replace(r"(","") \
        .replace(")","").replace(".","").replace("\n_anomesdia","").replace("\nanomesdia","") for x in dataframe.columns]

    # CLEAN DATA
    dataframe['FICHA'] = dataframe['FICHA'].astype(str)
    dataframe['FICHA'].ffill(axis = 0)
    dataframe['FICHA'] = [x.replace(".0","") for x in dataframe['FICHA']]
    dataframe['PROGRAMA_DE_FORMACION'].ffill(axis = 0)
    dataframe['PROGRAMA_DE_FORMACION'] = [x.replace(".","") for x in dataframe['PROGRAMA_DE_FORMACION']]
    dataframe['TIPO_DOCUMENTO'] = dataframe['TIPO_DOCUMENTO'].fillna('CC')
    dataframe['NUMERO_DE_DOCUMENTO'] = dataframe['NUMERO_DE_DOCUMENTO'].astype(str)
    dataframe['NUMERO_DE_DOCUMENTO'].ffill(axis = 0)
    dataframe['NOMBRE'].ffill(axis = 0)
    dataframe['APELLIDOS'].ffill(axis = 0)

    return dataframe
