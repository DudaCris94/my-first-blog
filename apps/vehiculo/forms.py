from django import forms

from models import Vehiculo


class VehiculoForm(forms.ModelForm):
	
	class Meta:
		model = Vehiculo

		fields = [
			'placa',
			'marca',
			'tipo',
			'color',
		]
		labels = {
			'placa' : 'Placa del Vehiculo',
			'marca' : 'Marca del Vehiculo',
			'tipo' : 'Modelo del Vehiculo',
			'color': 'Color del Vehiculo',
		}

		widgets = {
			'placa' : forms.TextInput(attrs={'class': 'form-control'}),
			'marca' : forms.TextInput(attrs={'class': 'form-control'}),
			'tipo' : forms.TextInput(attrs={'class': 'form-control'}),
			'color' : forms.TextInput(attrs={'class': 'form-control'}),
		}


class VehiculoForm2(forms.ModelForm):
	
	class Meta:
		model = Vehiculo

		fields = [
			'placa',
			'marca',
			'tipo',
			'color',
		]
		labels = {
			'placa' : 'Placa del Vehiculo',
			'marca' : 'Marca del Vehiculo',
			'tipo' : 'Modelo del Vehiculo',
			'color': 'Color del Vehiculo',
		}

		widgets = {
			'placa' : forms.TextInput(attrs={'class': 'form-control','readonly':'readonly','type':'text'}),
			'marca' : forms.TextInput(attrs={'class': 'form-control'}),
			'tipo' : forms.TextInput(attrs={'class': 'form-control'}),
			'color' : forms.TextInput(attrs={'class': 'form-control'}),
		}
