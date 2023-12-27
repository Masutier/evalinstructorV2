from django.db import models


# Run if there is no database
# -->    python manage.py migrate --database=staff_db --run-syncdb

class Instructor(models.Model):

    FICHA = models.CharField(max_length=9)
    PROGRAMA_DE_FORMACION = models.CharField(max_length=200, null=True)
    TIPO_DOCUMENTO = models.CharField(max_length=4)
    NUMERO_DE_DOCUMENTO = models.CharField(max_length=10)
    NOMBRE = models.CharField(max_length=150)
    APELLIDOS = models.CharField(max_length=150)
    PERFIL_DEL_INSTRUCTOR = models.CharField(max_length=200, null=True)
    FECHA_DEL_REPORTE = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.NOMBRE


class Aprendiz(models.Model):

    FICHA = models.CharField(max_length=9)
    TIPO_DE_DOCUMENTO = models.CharField(max_length=4)
    NUMERO_DE_DOCUMENTO = models.CharField(max_length=10)
    NOMBRE = models.CharField(max_length=150)
    APELLIDOS = models.CharField(max_length=150)
    CELULAR = models.CharField(max_length=10, null=True)
    CORREO_ELECTRONICO = models.CharField(max_length=200, null=True)
    ESTADO = models.CharField(max_length=50)
    FECHA_DEL_REPORTE = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.NOMBRE

