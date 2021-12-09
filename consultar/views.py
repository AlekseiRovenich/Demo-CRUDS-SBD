from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import DataClinic
from .models import Patient
from .forms import DataClinicForm, DataClinicFormNew, PatientFormNew

# Create your views here.
def consultar(request): # CONSULTA DE INFORMACION DESPUES DE LOS CAMBIOS DE PLANES
	submitted = False
	consulta_busqueda = 0
	dataclinic_list = DataClinic.objects.all()

	if request.method == "POST":
		if request.POST['input-busqueda']:
			print(request.POST['input-busqueda'])
			consulta_busqueda = request.POST['input-busqueda']
			return HttpResponseRedirect(f'/Consultar/?submitted=True&consulta_busqueda={consulta_busqueda}')
		else:
			return HttpResponseRedirect(f'/Consultar/?submitted=True')


	else:
		if 'submitted' in request.GET:
			if 'consulta_busqueda' in request.GET:
				consulta_busqueda = int(request.GET.get('consulta_busqueda'))

			submitted = True

	return render(request, 'consultar.html', 
		{'dataclinic': dataclinic_list, 'submitted': submitted, 'consulta_busqueda': consulta_busqueda})


def nuevaConsulta(request): # CONSULTA DE INFORMACION DESPUES DE LOS CAMBIOS DE PLANES
	submitted = False
	if request.method == "POST":
		form = DataClinicFormNew(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(f'/NuevaConsulta/?submitted=True')


	else:
		form = DataClinicFormNew
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'nueva_consulta.html', 
		{'submitted': submitted, 'form': form})


def update_consultar(request, consultar_id):
	submitted = False
	dataclinic_list = DataClinic.objects.get(pk=consultar_id)
	form = DataClinicForm(request.POST or None, instance=dataclinic_list)

	if form.is_valid():
		print('es valido')
		form.save()
		return redirect('consultar')
	
	return render(request, 'update_consultar.html',
		{'dataclinic': dataclinic_list, 'submitted': submitted, 'form': form})


def paciente(request): # ES LO QUE CONSULTA EL MEDICO DESPUES DE LOS CAMBIOS DE PLANES
	submitted = False
	consulta_busqueda = 0
	consulta_busqueda_paciente = 0
	patient_list = Patient.objects.all()
	dataclinic_list = DataClinic.objects.all()

	if request.method == "POST":
		if 'input-busqueda' in request.POST:
			print(request.POST['input-busqueda'])
			consulta_busqueda = request.POST['input-busqueda']
			return HttpResponseRedirect(f'/PersonalMedico/?submitted=True&consulta_busqueda={consulta_busqueda}')

		elif 'input-busqueda-paciente' in request.POST:
			print(request.POST['input-busqueda-paciente'])
			consulta_busqueda_paciente = request.POST['input-busqueda-paciente']
			return HttpResponseRedirect(f'/PersonalMedico/?submitted=True&consulta_busqueda_paciente={consulta_busqueda_paciente}')		
		else:
			return HttpResponseRedirect(f'/PersonalMedico/?submitted=True')


	else:
		if 'submitted' in request.GET:
			if 'consulta_busqueda' in request.GET:
				try:
					consulta_busqueda = int(request.GET.get('consulta_busqueda'))
				except:
					consulta_busqueda = 1

			if 'consulta_busqueda_paciente' in request.GET:
				try:
					consulta_busqueda_paciente = int(request.GET.get('consulta_busqueda_paciente'))
				except:
					consulta_busqueda_paciente = 1

			submitted = True

	return render(request, 'Paciente.html', {'dataclinic': dataclinic_list ,'patient': patient_list, 'submitted': submitted, 'consulta_busqueda': consulta_busqueda, 'consulta_busqueda_paciente': consulta_busqueda_paciente})


def nuevoPaciente(request): # CONSULTA DE INFORMACION DESPUES DE LOS CAMBIOS DE PLANES
	submitted = False
	if request.method == "POST":
		form = PatientFormNew(request.POST)
		print(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(f'/NuevoPaciente/?submitted=True')


	else:
		form = PatientFormNew
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'agregar_paciente.html', 
		{'submitted': submitted, 'form': form})


def update_paciente(request, paciente_id):
	submitted = False
	patient_list = Patient.objects.get(pk=paciente_id)
	form = PatientFormNew(request.POST or None, instance=patient_list)

	if form.is_valid():
		print('es valido')
		form.save()
		return redirect('pacientes')
	
	return render(request, 'update_paciente.html',
		{'patient_list': patient_list, 'submitted': submitted, 'form': form})


def delete_paciente(request, paciente_id):
	patient_list = Patient.objects.get(pk=paciente_id)
	patient_list.delete()
	return redirect('personal')


def personal(request): # DEPARTAMENTO DE IT DESPUES DE LOS CAMBIOS DE PLANES
	submitted = False
	consulta_busqueda = 0
	consulta_busqueda_paciente = 0
	patient_list = Patient.objects.all()
	dataclinic_list = DataClinic.objects.all()

	if request.method == "POST":
		if 'input-busqueda' in request.POST:
			print(request.POST['input-busqueda'])
			consulta_busqueda = request.POST['input-busqueda']
			return HttpResponseRedirect(f'/Personal/?submitted=True&consulta_busqueda={consulta_busqueda}')

		elif 'input-busqueda-paciente' in request.POST:
			print(request.POST['input-busqueda-paciente'])
			consulta_busqueda_paciente = request.POST['input-busqueda-paciente']
			return HttpResponseRedirect(f'/Personal/?submitted=True&consulta_busqueda_paciente={consulta_busqueda_paciente}')		
		else:
			return HttpResponseRedirect(f'/Personal/?submitted=True')


	else:
		if 'submitted' in request.GET:
			if 'consulta_busqueda' in request.GET:
				try:
					consulta_busqueda = int(request.GET.get('consulta_busqueda'))
				except:
					consulta_busqueda = 1

			if 'consulta_busqueda_paciente' in request.GET:
				try:
					consulta_busqueda_paciente = int(request.GET.get('consulta_busqueda_paciente'))
				except:
					consulta_busqueda_paciente = 1

			submitted = True

	return render(request, 'Personal.html', {'dataclinic': dataclinic_list ,'patient': patient_list, 'submitted': submitted, 'consulta_busqueda': consulta_busqueda, 'consulta_busqueda_paciente': consulta_busqueda_paciente})

def agregarPersonal(request):
	return render(request, 'agregar_personal.html')

def agregarPaciente(request):
	return render(request, 'agregar_paciente.html')
