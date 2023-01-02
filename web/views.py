from django.shortcuts import render
from web.models import UbicacionForm, Ubicacion

def home(request):
    ubicaciones = Ubicacion.objects.all()
    form = UbicacionForm()
    return render (request,"index.html",{'ubicaciones':ubicaciones})


def recibir_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        lat = request.POST['lat']
        lng = request.POST['lng']
        m = Ubicacion(nombre=nombre, lat=lat,lng=lng)
        m.save()
        return render(request, 'recibido.html')
    return render(request, 'recibir_mensaje.html')
