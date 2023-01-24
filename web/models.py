from django.db import models
from django.forms import ModelForm

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=20)
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)
    contaminacion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.nombre


class UbicacionForm(ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['lat', 'lng','nombre']
