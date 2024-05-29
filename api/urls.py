from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import usuarios_api_view, usuarios_detail_view, usuario_log_view, usr_reg, usr_program_view

router = routers.DefaultRouter()
router.register(r'programa', views.ProgramaviewSet)
router.register(r'workout', views.EntrenamientoViewSet)
router.register(r'ejercicio', views.EjercicioViewSet)
router.register(r'meal', views.AlimentacionViewSet)
router.register(r'comida', views.ComidaViewSet)
router.register(r'sleep', views.SleepViewSet)
router.register(r'today', views.TodayView)
router.register(r'find', views.FindEatViewSet)
router.register(r'categ', views.CategoriaView)
router.register(r'pop', views.PopularView)
router.register(r'recom', views.RecomendadoView)
router.register(r'des', views.DesayunoView)
router.register(r'alm', views.AlmuerzoView)
router.register(r'cena', views.CenaView)
router.register(r'snack', views.SnackView)
router.register(r'nutri', views.NutricionView)
router.register(r'nuttri', views.NutritionView)
router.register(r'ingre', views.IngredienteView)
router.register(r'paso', views.PasoView)
router.register(r'hoy', views.HoyView)
router.register(r'evt', views.EventoView)
router.register(r'you', views.YouView)
router.register(r'late', views.LateView)
router.register(r'eje', views.EjeView)


urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/', usuarios_api_view, name= 'usuarios'),
    path('usuarios/<int:pk>', usuarios_detail_view, name= 'usuarios_detail'),
    path('usuarios/log', usuario_log_view, name='user_log'),
    path('usr/reg', usr_reg, name='user_reg'),
    path('usr/upt', usr_program_view, name='usr_upt')
    
]