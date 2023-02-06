from django.shortcuts import render
from web.models import UbicacionForm, Ubicacion
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def receive_json(request):
    if request.method == 'POST':
        # Analizar el cuerpo de la petición como un JSON
        json_data = json.loads(request.body)
        try:
            lt = float(json_data['lat'])
            lg = float(json_data['lng'])
            if not -90 <= lt <= 90:
                raise ValueError('Latitude must be between -90 and 90')
            if not -180 <= lg <= 180:
                raise ValueError('Longitude must be between -180 and 180')
        except (KeyError, ValueError) as e:

            return JsonResponse({'error': str(e)})

        # Aquí puedes guardar la información en tu base de datos        
        #print(type(json_data[0]['nombre']))
        my_model = Ubicacion(nombre=json_data['nombre'], lat=json_data['lat'], lng= json_data['lng'],contaminacion=json_data['contaminacion'])
        my_model.save()
        # Devolver una respuesta al script de Python
        return JsonResponse({'status': 'success'})
        
    else:
        # Devolver un error si la petición no es del tipo POST
        return JsonResponse({'error': 'Invalid request method'})
def guardar_peticion(request):
    if request.method == 'POST':
        # Obtén los datos enviados en la solicitud
        data = request.POST
        # Crea una instancia del modelo Ubicacion con los datos recibidos
        ubicacion = Ubicacion(Nombre=data['Nombre'], lat=data['lat'], lang=data['lang'])
        # Guarda la instancia en la base de datos
        ubicacion.save()
        # Devuelve una respuesta exitosa
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def home(request):
    ubicaciones = Ubicacion.objects.all()
    form = UbicacionForm()
    listaUbicaciones = []
    for ubi in ubicaciones:
        listaUbicaciones.append([ubi.nombre,ubi.lat,ubi.lng,ubi.contaminacion,str(ubi.fecha)])
    return render (request,"index.html",{'ubicaciones':listaUbicaciones})
