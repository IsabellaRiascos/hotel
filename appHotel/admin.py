from django.contrib import admin

# Register your models here.
from appHotel.models import Habitacion,TipoHabitacion,Cliente,Reserva,Pago,TipoReserva

admin.site.register(Habitacion)
admin.site.register(TipoHabitacion)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(TipoReserva)
