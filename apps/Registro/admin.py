from django.contrib import admin
from .models import Usuario, Cliente, Contacto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Contacto)
