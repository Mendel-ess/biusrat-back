from django.db import models

# Create your models here.

class Programa(models.Model):
    nombre_programa = models.CharField(max_length=50)
    descrip_programa = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.nombre_programa

class Entrenamiento(models.Model):
    tipo_entrenamiento = models.CharField(max_length=50)
    dificultad = models.CharField(max_length=50)
    image = models.TextField(default="assets/images/what_1.png")
    time = models.TextField(default="3 ejercicios")
    exercises = models.TextField(default="1 hora")
    id_programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tipo_entrenamiento

class Ejercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=50)
    descrip_ejercicio = models.TextField()
    serie = models.IntegerField()
    repeticion = models.IntegerField()
    peso = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default="assets/images/img_1.png")
    id_entrenamiento = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_ejercicio

class Alimentacion(models.Model):
    comida_tiempo = models.CharField(max_length=50)
    id_programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return self.comida_tiempo

class Comida(models.Model):
    nombre_plato = models.CharField(max_length=100)
    calorias = models.IntegerField()
    cant_proteinas = models.IntegerField()
    cant_grasas = models.IntegerField()
    cant_carbo = models.IntegerField()
    id_alimentacion = models.ForeignKey(Alimentacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_plato

class Usuarios(models.Model):
    correo = models.EmailField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=50,null=True, blank=True)
    password = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=60, null=True, blank=True)
    peso = models.IntegerField(null=True, blank=True)
    altura = models.IntegerField(null=True, blank=True)
    id_programa = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.correo

class Sleep(models.Model):
    hora_acostarse = models.DateTimeField()
    hora_levantarse = models.DateTimeField()
    cant_horas = models.IntegerField()
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.hora_acostarse
    
class TodayMeal(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

class FindEat(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    number = models.CharField(max_length=100)


class Categoria(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

class Popular(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    b_image = models.CharField(max_length=200)
    size = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    kcal = models.CharField(max_length=50)

class Recomendado(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    size = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    kcal = models.CharField(max_length=50)

class Desayuno(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    image = models.CharField(max_length=200)

class Almuerzo(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    image = models.CharField(max_length=200)

class Snack(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    image = models.CharField(max_length=200)

class Cena(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    image = models.CharField(max_length=200)

class Nutricion(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    unit_name = models.CharField(max_length=10)
    value = models.CharField(max_length=10)
    max_value = models.CharField(max_length=10)

class Nutrition(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=100)

class Ingredientes(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Paso(models.Model):
    no = models.CharField(max_length=10)
    detail = models.TextField()

class HoySleep(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

class Evento(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)   

class Latest(models.Model):
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

class You(models.Model):
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class EjeSet(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Eje(models.Model):
    exercise_set = models.ForeignKey(EjeSet, related_name='exercises', on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)