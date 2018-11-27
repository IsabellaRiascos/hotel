from rest_framework import serializers
from .models import Cliente, Habitacion, Pago, Reserva, TipoHabitacion, TipoReserva

class HabitacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habitacion
        fields = ('__all__')


class TipoHabitacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = ('__all__')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')        

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')


class PagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pago
        fields = ('__all__')


class TipoReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoReserva
        fields = ('__all__')