from django.contrib import admin
from .models import Anfitrion

class AnfitrionAdmin(admin.ModelAdmin): # por si necesito personalizarlo
    pass

admin.site.register(Anfitrion, AnfitrionAdmin)