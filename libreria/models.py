from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="imagen", null=True)
    descripcion = models.TextField(verbose_name="descripcion", null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "descripcion: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank = True)        

