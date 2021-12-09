from django import forms
from django.forms import ModelForm
from .models import DataClinic
from .models import Patient

# dataclinic form
class DataClinicForm(ModelForm):
	class Meta:
		model = DataClinic
		# NO SE COLOCARON LOS BOOLEANOS, SI HAY UN ID ES PORQUE ES TRUE
		fields = ('vreasonconsult', 'vinitialdx', 'vdifferentialdx', 'iexamid', 'ispecialistid', 'iprescriptionid', 'dcheckupdate')

		labels = {
			'vreasonconsult': '', 
			'vinitialdx': '',
			'vdifferentialdx': '',
			#'iexamid'
			#'ispecialistid'
			#'iprescriptionid'
			'dcheckupdate': ''	
		}

		widgets = {
			'vreasonconsult': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'razon de consulta'}), 
			'vinitialdx': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'diagnostico inicial'}),
			'vdifferentialdx': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'diagnostico diferencial'}),
			#'iexamid'
			#'ispecialistid'
			#'iprescriptionid'
			'dcheckupdate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'checkup date'})	
		}

class DataClinicFormNew(ModelForm):
	class Meta:
		model = DataClinic
		# NO SE COLOCARON LOS BOOLEANOS, SI HAY UN ID ES PORQUE ES TRUE
		fields = "__all__"

		labels = {
			'vreasonconsult': '', 
			'vinitialdx': '',
			'vdifferentialdx': '',
			#'iexamid'
			#'ispecialistid'
			#'iprescriptionid'
			'dcheckupdate': ''	
		}

		widgets = {
			'vreasonconsult': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'razon de consulta'}), 
			'vinitialdx': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'diagnostico inicial'}),
			'vdifferentialdx': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'diagnostico diferencial'}),
			#'iexamid'
			#'ispecialistid'
			#'iprescriptionid'
			'dcheckupdate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'checkup date'})	
		}

class PatientFormNew(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

        # labels = {
        #   #  'ipatientid':'',
        #   #  'idataadminid':'',
        #   #  'idataclinicid':'',
        #   #  'ipersonelid':'',
        #   #  'tage':'',
        #   #  'csex':'',
        #   #  'thealth':'',
        #   #  'bpatientstatus':'',
        #   #  'vfullname':'',
        #    # 'ibloodtypeid':'',
        #    # 'iantigenid':'',
        #   #  'comorbility':''
        # }

        # widget = {
        #     #'ipatientid':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID del paciente'}),
        #     #'idataadminid':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID de su formato administrativo'}),
        #     #'idataclinicid':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID de su formato clinico'}),
        #     #'ipersonelid':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID del Medico'}),
        #     #'tage':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'edad del paciente'}),
        #     #'csex':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'M/F'}),
        #     #'thealth':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID del Estado de Salud del paciente'}),
        #     #'bpatientstatus':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'0 = inactivo /1 = activo'}),
        #     #'vfullname':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'nombre completo'}),
        #     #'ibloodtypeid':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID de su tipo de sangre'}),
        #     #'iantigenid':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'1 = positivo (+) / 2 = negativo (-)'}),
        #     'comorbility':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ID comorbilidad del paciente'}),
        # }