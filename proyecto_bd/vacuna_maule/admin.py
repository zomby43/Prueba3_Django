from django.contrib import admin

# Register your models here.


from vacuna_maule.models import Vacuna
admin.site.register(Vacuna)

from vacuna_maule.models import Trabajador
admin.site.register(Trabajador)

