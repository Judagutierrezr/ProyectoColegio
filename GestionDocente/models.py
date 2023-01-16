from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profesor(models.Model):
    Nombre=models.CharField(max_length=15)
    Apellido=models.CharField(max_length=15)
    Titulo=models.CharField(max_length=25)
    Email = models.EmailField()
    Telefono = models.IntegerField()
    def __str__(self):
        return self.Nombre +" "+ self.Apellido 
    
class Grado(models.Model):
    Nombre=models.CharField(max_length=15)
    def __str__(self):
        return self.Nombre

class Curso(models.Model):
    Nombre=models.CharField(max_length=15)
    Grado=models.ForeignKey(Grado,on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre

class Asignatura(models.Model):
    Nombre=models.CharField(max_length=25)
    Descripcion=models.CharField(max_length=15,null=True, blank=True)
    Horas=models.IntegerField()

    def __str__(self):
        return self.Nombre

class Estudiante(models.Model):
    Nombre=models.CharField(max_length=15)
    Apellido=models.CharField(max_length=15)
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre +" "+ self.Apellido 


class Indicadores_Desempeño(models.Model):
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    Asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    Periodo_Uno_Competencia=models.CharField(max_length=500,null=True, blank=True)
    Periodo_Uno_1=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Uno_2=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Uno_3=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Dos_Competencia=models.CharField(max_length=500,null=True, blank=True)
    Periodo_Dos_1=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Dos_2=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Dos_3=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Tres_Competencia=models.CharField(max_length=500,null=True, blank=True)
    Periodo_Tres_1=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Tres_2=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Tres_3=models.TextField(max_length=500,null=True, blank=True)
    def __str__(self):
       return self.Asignatura.Nombre
    

class Asignacion_De_Curso(models.Model):
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    Profesor=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Profesor +" "+ self.Asignatura+"  "+ self.Curso

class Historico(models.Model):
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Profesor = models.ForeignKey(User,on_delete=models.CASCADE,default=User.USERNAME_FIELD)
    Fecha=models.DateField(auto_now_add=True, auto_now=False)
    Comentario_Docente=models.TextField(max_length=500,null=True, blank=True)
    Comentario_Estudiante=models.TextField(max_length=500,null=True, blank=True)

class Convivencia(models.Model):
    Profesor = models.ForeignKey(User,on_delete=models.CASCADE,default=User.USERNAME_FIELD)
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Fecha=models.DateField(auto_now_add=True, auto_now=False)
    Hora = models.TimeField(auto_now_add=True, auto_now=False)
    Comentario_Docente=models.TextField(max_length=500,null=True, blank=True)
    Comentario_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    FaltaTipo= models.CharField(max_length=15)
    Compromiso_de_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    Recurrente= models.BooleanField(default=False)
    Cita_Acudientes= models.DateField(null=True)
    Puntos_negativos=models.PositiveIntegerField(default=1)

class Psicoorientacion(models.Model):
    psicoorientador = models.ForeignKey(User,on_delete=models.CASCADE,default=User.USERNAME_FIELD)
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Fecha=models.DateField(auto_now_add=True, auto_now=False)
    Hora = models.TimeField(auto_now_add=True, auto_now=False)
    Comentario_Docente=models.TextField(max_length=500,null=True, blank=True)
    Comentario_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    Colsulta_tipo= models.CharField(max_length=15)
    Compromiso_de_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    Recurrente= models.BooleanField(default=False)
    Proxima_cita= models.DateField(null=True)
    Evidencias = models.ImageField(upload_to="PSICOLOGIA",null=True)
    




    
    