from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "Registro/listar_clientes.html", {'clientes': clientes})


def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_cliente")
    else:
        form = ClienteForm()
        return render(request, "Registro/agregar_cliente.html", {'form': form})

def borrar_cliente(request, cliente_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Cliente.objects.get(id=cliente_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_clientes')

def editar_cliente(request, cliente_id):
    # Recuperamos la instancia de la carrera
    instancia = Cliente.objects.get(id=cliente_id)

    # Creamos el formulario con los datos de la instancia
    form = ClienteForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ClienteForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_cliente.html", {'form': form})
