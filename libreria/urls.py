from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros',views.libros, name='libros'),
    path('libros/crear',views.crear, name='crear'),
    path('libros/editar',views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('libros/editar<int:id>',views.editar, name='editar'),
    path('loginvista', views.login_request, name='loginvista'),
    path('registrarvista', views.register, name='registrarvista'),
    path('comentar', views.comentar, name='comentar'),
    path("editarperfil" , views.editarperfil , name="editarperfil"),
    
    
    
    
    
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)