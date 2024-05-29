from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404

@api_view(['PUT'])
def usr_program_view(request):
    if request.method == 'PUT':
        correo = request.data.get('correo')
        id_programa = request.data.get('id_programa')
        usr = Usuarios.objects.filter(correo=correo).first()
        if usr:
            programa = get_object_or_404(Programa, id=id_programa)
            usr.id_programa = programa
            usr.save()
            return Response({'message': 'Programa asignado'}, status=202)
        

@api_view(['POST'])
def usuario_log_view(request):

    if request.method == 'POST':
        correo = request.data.get('correo')
        password = request.data.get('password')
        usuario = Usuarios.objects.filter(correo=correo, password=password).first()

        if usuario:
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def usr_reg(request):
    if request.method == 'POST':
        nombre = request.data.get('nombre')
        apellido = request.data.get('apellido')
        correo = request.data.get('correo')
        password = request.data.get('password')
        genero = request.data.get('genero')
        fecha_nacimiento = request.data.get('fecha_nacimiento')
        peso = request.data.get('peso')
        altura = request.data.get('altura')

        usr_exist = Usuarios.objects.filter(correo=correo).first()

        if usr_exist:
            return Response({'error': 'Usuario ya existe'}, status=400)

        usr = Usuarios(nombre=nombre, apellido=apellido, correo=correo, password=password, genero=genero, fecha_nacimiento=fecha_nacimiento, peso=peso, altura=altura)
        usr.save()
        usr_serializer = UsuariosSerializer(usr)
        return Response(status=201)

@api_view(['GET', 'POST'])
def usuarios_api_view(request):

    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        usuarios_serializer = UsuariosSerializer(usuarios, many=True) 
        return Response(usuarios_serializer.data)
    
    if request.method == 'POST':
        pass
    
@api_view(['GET'])
def usuarios_detail_view(request,pk):
    if request.method == 'GET':
        usuario = Usuarios.objects.filter(id = pk).first()
        usuario_serializer = UsuariosSerializer(usuario)
        return Response(usuario_serializer.data)


class ProgramaviewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

class EntrenamientoViewSet(viewsets.ModelViewSet):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer


class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class AlimentacionViewSet(viewsets.ModelViewSet):
    queryset = Alimentacion.objects.all()
    serializer_class = AlimentacionSerializer

class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer

class SleepViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

class FindEatViewSet(viewsets.ModelViewSet):
    queryset = FindEat.objects.all()
    serializer_class = FindSerializer

class TodayView(viewsets.ModelViewSet):
    queryset = TodayMeal.objects.all()
    serializer_class = TodaySerializer

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PopularView(viewsets.ModelViewSet):
    queryset = Popular.objects.all()
    serializer_class = PopularSerializer

class RecomendadoView(viewsets.ModelViewSet):
    queryset = Recomendado.objects.all()
    serializer_class = RecomendadoSerializer

class DesayunoView(viewsets.ModelViewSet):
    queryset = Desayuno.objects.all()
    serializer_class = DesayunoSerializer

class AlmuerzoView(viewsets.ModelViewSet):
    queryset = Almuerzo.objects.all()
    serializer_class = AlmuerzoSerializer

class SnackView(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class CenaView(viewsets.ModelViewSet):
    queryset = Cena.objects.all()
    serializer_class = CenaSerializer

class NutricionView(viewsets.ModelViewSet):
    queryset = Nutricion.objects.all()
    serializer_class = NutricionSerializer

class NutritionView(viewsets.ModelViewSet):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializer

class IngredienteView(viewsets.ModelViewSet):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredienteSerializer

class PasoView(viewsets.ModelViewSet):
    queryset = Paso.objects.all()
    serializer_class = PasoSerializer

class HoyView(viewsets.ModelViewSet):
    queryset = HoySleep.objects.all()
    serializer_class = HoySleepSerializer

class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class LateView(viewsets.ModelViewSet):
    queryset = Latest.objects.all()
    serializer_class = LateSerializer

class YouView(viewsets.ModelViewSet):
    queryset = You.objects.all()
    serializer_class = youSerializer

class EjeView(viewsets.ModelViewSet):
    queryset = Eje.objects.all()
    serializer_class = EjeSerializer