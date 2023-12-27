from loadings.models import *


def apprend(documento):
    documento = request.session['aprendiz']
    aprendix = Aprendiz.objects.using('staff_db').get(NUMERO_DE_DOCUMENTO = documento)

    print('apprend', aprendix)
    return aprendix