from django.shortcuts import render, redirect
from .models import Caninos
from .forms import CaninoForm
from django.core.mail import send_mail

# Vista para listar todos los caninos
def listar_caninos(request):
    caninos = Caninos.objects.all()
    return render(request, 'listar_caninos.html', {'caninos': caninos})

# Vista para agregar un nuevo canino
def agregar_canino(request):
    if request.method == 'POST':
        form = CaninoForm(request.POST)
        if form.is_valid():
            form.save()
            # Enviar correo (ejemplo de confirmación)
            send_mail(
                'Nuevo canino agregado',
                'Se ha agregado un nuevo canino a la base de datos.',
                'from@example.com',
                ['admin@example.com'],
                fail_silently=False,
            )
            return redirect('listar_caninos')
    else:
        form = CaninoForm()
    return render(request, 'agregar_canino.html', {'form': form})