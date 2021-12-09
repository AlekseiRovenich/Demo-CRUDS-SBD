"""Consultorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from consultar import views as ConsultarViews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Consultar/', ConsultarViews.consultar, name='consultar'),
    path('NuevaConsulta/', ConsultarViews.nuevaConsulta, name='nueva-consulta'),
    path('Update-Consultar/<consultar_id>', ConsultarViews.update_consultar, name='update_consultar'),

    path('Personal/', ConsultarViews.personal, name='personal'),

    path('PersonalMedico/', ConsultarViews.paciente, name='pacientes'),
    path('NuevoPaciente/', ConsultarViews.nuevoPaciente, name='nuevo-paciente'),
    path('Update-Paciente/<paciente_id>', ConsultarViews.update_paciente, name='update_paciente'),
    path('Delete-Patient/<paciente_id>', ConsultarViews.delete_paciente, name='delete_paciente'),

    path('Agregar-Personal/', ConsultarViews.agregarPersonal, name='agregarPersonal'),
    path('Agregar-Paciente/', ConsultarViews.agregarPaciente, name='agregarPaciente')
]
