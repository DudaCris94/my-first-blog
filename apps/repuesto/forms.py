from django import forms

from models import Repuesto


class RepuestoForm(forms.ModelForm):
	
	class Meta:
		model = Repuesto

		fields = [
			'detalle',
			'orden',
			'precio',
			'adquisicion',
			'fechaCambio',
			'responsable',
			'kilometraje',
		]
		labels = {
			'detalle' : 'Detalle del Repuesto',
			'orden' : 'Numero de Orden',
			'precio' : 'Precio',
			'adquisicion': 'Lugar donde se adquirio el Repuesto',
			'fechaCambio': 'Fecha de cambio',
			'responsable':'Vehiculo al que se le aplica el Repuesto',
			'kilometraje': 'Kilometraje actual del Vehiculo',
			
		}

		widgets = {
			'detalle' : forms.TextInput(attrs={'class': 'form-control'}),
			'orden' : forms.TextInput(attrs={'class': 'form-control'}),
			'precio' :  forms.TextInput(attrs={'class': 'form-control'}),
			'adquisicion' : forms.Select(attrs={'class': 'form-control'}),
			'fechaCambio' :  forms.TextInput(attrs={'class': 'form-control','type':'date'}),
			'responsable' : forms.Select(attrs={'class': 'form-control'}),
			'kilometraje' : forms.TextInput(attrs={'class': 'form-control'}),

			
		}




class RepuestoForm2(forms.ModelForm):
	
	class Meta:
		model = Repuesto


		fields = [
			'detalle',
			'orden',
			'precio',
			'adquisicion',
			'fecha',
			'fechaCambio',
			'responsable',
			'kilometraje',
		]

		labels = {
			'detalle' : 'Detalle del Repuesto',
			'orden' : 'Numero de Orden',
			'precio' : 'Precio Actual',
			'adquisicion': 'Lugar donde se adquirio el Repuesto',
			'fecha': 'Fecha del Cambio mas Reciente',
			'fechaCambio': 'Fecha del Ultimo Cambio',
			'responsable':'Vehiculo al que se le aplica el Repuesto',
			'kilometraje': 'Kilometraje actual del Vehiculo',
			
		}

		
		widgets = {
			'detalle' : forms.TextInput(attrs={'class': 'form-control','readonly':'readonly','type':'text'}),
			'orden' :  forms.TextInput(attrs={'class': 'form-control'}),
			'precio' :  forms.TextInput(attrs={'class': 'form-control'}),
			'adquisicion' : forms.Select(attrs={'class': 'form-control'}),
			'fecha' :  forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
			'fechaCambio' :  forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
			'responsable' : forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
			'kilometraje' : forms.TextInput(attrs={'class': 'form-control'}),
		}
		
