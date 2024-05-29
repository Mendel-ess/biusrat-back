from rest_framework import serializers
from .models import *
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'correo', 'nombre', 'apellido', 'genero', 'password', 'fecha_nacimiento', 'peso', 'altura', 'id_programa')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuarios.objects.create_user(
            correo=validated_data['correo'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            genero=validated_data.get('genero', ''),
            password=validated_data['password'],
            fecha_nacimiento=validated_data.get('fecha_nacimiento', None),
            peso=validated_data.get('peso', None),
            altura=validated_data.get('altura', None),
            id_programa=validated_data.get('id_programa', None)
        )
        return usuario

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'

class EntrenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenamiento
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class ComidaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comida
        fields = '__all__'

class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = '__all__'

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = '__all__'

class TodaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayMeal
        fields = '__all__'

class FindSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindEat
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        fields = '__all__'

class RecomendadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendado
        fields = '__all__'

class DesayunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desayuno
        fields = '__all__'

class AlmuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almuerzo
        fields = '__all__'

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = '__all__'

class CenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cena
        fields = '__all__'

class NutricionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricion
        fields = '__all__'

class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = '__all__'

class PasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paso
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'

class HoySleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoySleep
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class LateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latest
        fields = '__all__'

class youSerializer(serializers.ModelSerializer):
    class Meta:
        model = You
        fields = '__all__'

class EjeSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EjeSet
        fields = '__all__'

class EjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eje
        fields = '__all__'