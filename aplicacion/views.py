

# Create your views here.
from django.shortcuts import render
from .forms import CustomForm

def formulario_vista(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario aquí
            opciones_seleccionadas = form.cleaned_data['opciones']
            hora_seleccionada = form.cleaned_data['hora']
            # Aquí puedes realizar más acciones con los datos
            return render(request, 'success.html')
    else:
        form = CustomForm()

    return render(request, 'formulario.html', {'form': form})


