import openpyxl as op 
from tabulate import tabulate

from django.http import HttpResponse
from django.template import Template, Context

def app(request): #primera vista
    doc_externo = open("Proyecto_aula/plantillas/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def getFile(request):
    
    excel_dataFrame = op.load_workbook(request.POST['customFile'])
    print(excel_dataFrame)