from django.shortcuts import render
from django.http import HttpResponse
from appHotel.models import Habitacion, TipoHabitacion,Cliente,Reserva,Pago,TipoReserva
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import ClienteSerializer, HabitacionSerializer, PagoSerializer, ReservaSerializer, TipoHabitacionSerializer,TipoReservaSerializer 


# Create your views here.



def first_view(request):
    return render(request, 'base.html')

def habitacion(request):
	habitacion_list = Habitacion.objects.all()
	context = {'object_list': habitacion_list}
	return render(request,'hotel/habitacion.html',context)


def habitacion_detail(request, habitacion_id):
	habitacion = Habitacion.objects.get(id=habitacion_id)
	context = {'object':habitacion}
	return render(request, 'hotel/habitacion_detail.html',context)

class HabitacionUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=Habitacion
	fields = '__all__'

class HabitacionCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= Habitacion
	fields = '__all__'


class HabitacionDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= Habitacion
	success_url = reverse_lazy('habitacion-list')

#Para la clase TipoHabitacion

class TipoHabitacionListView(ListView):
	"""docstring for PhotoListView"""
	model = TipoHabitacion

class TipoHabitacionDetailView(DetailView):
	"""docstring for PhotoDetailView"""
	model= TipoHabitacion

class TipoHabitacionUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=TipoHabitacion
	fields = '__all__'

class TipoHabitacionCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= TipoHabitacion
	fields = '__all__'
	
class TipoHabitacionDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= TipoHabitacion
	success_url = reverse_lazy('tipohabitacion-list')

#Para la clase Cliente

class ClienteListView(ListView):
	"""docstring for PhotoListView"""
	model = Cliente


class ClienteDetailView(DetailView):
	"""docstring for PhotoDetailView"""
	model= Cliente


class ClienteUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=Cliente
	fields = '__all__'


class ClienteCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= Cliente
	fields = '__all__'

class ClienteDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= Cliente
	success_url = reverse_lazy('cliente-list')


#Para la clase PAGO

class PagoListView(ListView):
	"""docstring for PhotoListView"""
	model = Pago


class PagoDetailView(DetailView):
	"""docstring for PhotoDetailView"""
	model= Pago


class PagoUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=Pago
	fields = '__all__'


class PagoCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= Pago
	fields = '__all__'
	

class PagoDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= Pago
	success_url = reverse_lazy('pago-list')

#Para la clase RESERVA


class ReservaListView(ListView):
	"""docstring for ReservaListView"""
	model = Reserva


class ReservaDetailView(DetailView):
	"""docstring for ReservaDetailView"""
	model= Reserva


class ReservaUpdate(UpdateView):
	"""docstring for ReservaUpdate"""
	model=Reserva
	fields = '__all__'


class ReservaCreate(CreateView):
	"""docstring for ReservaCreate"""
	model= Reserva
	fields = '__all__'

class ReservaDelete(DeleteView):
	"""docstring for ReservaDelete"""
	model= Reserva
	success_url = reverse_lazy('reserva-list')

#Para la clase TIPO DE RESERVA

class TipoReservaListView(ListView):
	"""docstring for ReservaListView"""
	model = TipoReserva

class TipoReservaDetailView(DetailView):
	"""docstring for ReservaDetailView"""
	model= TipoReserva

class TipoReservaUpdate(UpdateView):
	"""docstring for ReservaUpdate"""
	model=TipoReserva
	fields = '__all__'

class TipoReservaCreate(CreateView):
	"""docstring for ReservaCreate"""
	model= TipoReserva
	fields = '__all__'
	
class TipoReservaDelete(DeleteView):
	"""docstring for ReservaDelete"""
	model= TipoReserva
	success_url = reverse_lazy('tiporeserva-list')
# Create your views here.


#----------------------serializers--------------------------

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


class PagoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class TipoHabitacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer


class TipoReservaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoReserva.objects.all()
    serializer_class = TipoReservaSerializer