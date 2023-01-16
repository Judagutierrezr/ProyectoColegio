from django.urls import path
from GestionDocente import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Vregistro, logear


urlpatterns = [
    path('', views.home, name="Home"),
    path('home', views.home, name="Home"),
    path('docente', views.docente, name="Docente"),
    path('estudiante', views.estudiante, name="Estudiantes"),
    path('autenticacion', Vregistro.as_view(), name="Autenticacion"),
    path('login', logear, name="logear"),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
