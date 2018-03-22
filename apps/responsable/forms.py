from django import forms

from models import Responsable


class ResponsableForm(forms.ModelForm):
	
	class Meta:
		model = Responsable

		fields = [
			'nombre',
			'apellidos',
			'cedula',
			'cargo',
			'vehiculo',
		]
		labels = {
			'nombre' : 'Nombres',
			'apellidos' : 'Apellidos',
			'cedula' : 'Numero de Cedula',
			'cargo': 'Cargo en la Escuela',
			'vehiculo': 'Vehiculo Asignado a su Tutela'
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos' : forms.TextInput(attrs={'class': 'form-control'}),
			'cedula' : forms.TextInput(attrs={'class': 'form-control'}),
			'cargo' : forms.TextInput(attrs={'class': 'form-control'}),
			'vehiculo' : forms.Select(attrs={'class': 'form-control'}),
		}


class ResponsableForm2(forms.ModelForm):
	
	class Meta:
		model = Responsable

		fields = [
			'nombre',
			'apellidos',
			'cedula',
			'cargo',
			'vehiculo',
		]
		labels = {
			'nombre' : 'Nombres',
			'apellidos' : 'Apellidos',
			'cedula' : 'Numero de Cedula',
			'cargo': 'Cargo en la Escuela',
			'vehiculo': 'Vehiculo Asignado a su Tutela'
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control','readonly':'readonly','type':'text'}),
			'apellidos' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly','type':'text'}),
			'cedula' : forms.TextInput(attrs={'class': 'form-control'}),
			'cargo' : forms.TextInput(attrs={'class': 'form-control'}),
			'vehiculo' : forms.Select(attrs={'class': 'form-control'}),
		}