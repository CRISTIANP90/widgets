from django import forms

class CustomForm(forms.Form):
    opciones = forms.MultipleChoiceField(
        choices=[
            ('opcion1', 'Opción 1'),
            ('opcion2', 'Opción 2'),
            ('opcion3', 'Opción 3'),
        ],
        widget=forms.SelectMultiple,
        label="Seleccione una o más opciones"
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Seleccione la hora"
    )
