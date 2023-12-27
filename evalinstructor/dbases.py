import os
import json
from django.conf import settings
from .confSett import securFileHome, securFileSena

SENA = False

if SENA:
    config = securFileSena()
else:
    config = securFileHome()



# **************************************** https://vuyisile.com/how-to-use-django-with-multiple-databases/
# ****************************************>    https://www.youtube.com/watch?v=g-FCzzzjBWo     <**********
# **************************************** https://www.youtube.com/watch?v=LazPUV13USE
# **************************************** https://www.youtube.com/watch?v=dBiC9XKf4pc



def extensions():
    validExt = ['csv', 'json', 'xlsx', 'pdf', 'html', 'xml', 'sql', 'db', 'py', 'css', 'js']
    validExtPro = ['csv', 'json', 'xlsx', 'xml']
    return validExt, validExtPro


def dbSqlite(BASE_DIR):

    return None
    


