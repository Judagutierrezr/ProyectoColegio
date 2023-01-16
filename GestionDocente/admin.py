from urllib import request
from django.contrib import admin
from GestionDocente.models import Profesor, Asignatura, Estudiante, Curso,  Indicadores_Desempeño, Grado, Asignacion_De_Curso, Historico, Convivencia,Psicoorientacion
from django.contrib.auth.models import User

# Register your models here.

class ProfesAdmin(admin.ModelAdmin):
    list_display=("Nombre","Apellido","Telefono")
    search_fields=("Nombre","Apellido") 

class Asignacion(admin.ModelAdmin):
    list_display=("Curso","Asignatura","Profesor")

class Orden_Materias(admin.ModelAdmin):
    ordering=('Nombre','Horas')

class HistoricoVista(admin.ModelAdmin):
    search_fields=("Nombre","Apellido") 
    list_display=("Estudiante","Fecha","Profesor")

class ConvivenciaVista(admin.ModelAdmin):
    search_fields=("Nombre","Apellido") 
    list_display=("Estudiante","Fecha","Hora","Comentario_Docente","FaltaTipo","Cita_Acudientes")
 
class PsicoorientacionVista(admin.ModelAdmin):
    search_fields=("Nombre","Apellido") 
    list_display=("Estudiante","Fecha","Hora","psicoorientador","Proxima_cita")


#admin.site.register(Profesor, ProfesAdmin)
admin.site.register(Grado)
admin.site.register(Asignatura, Orden_Materias)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Indicadores_Desempeño)
admin.site.register(Asignacion_De_Curso)
admin.site.register(Historico, HistoricoVista)
admin.site.register(Convivencia, ConvivenciaVista)
admin.site.register(Psicoorientacion, PsicoorientacionVista)

