import fractions
from django.http import HttpResponse
from django.template import Context, Template

def template(self):


    template = open("C:/Users/Santi/Desktop/proyecto1/template.html")

    plantilla = Template(template.read())

    template.close()
    
    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)