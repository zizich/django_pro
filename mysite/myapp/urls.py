from django.urls import path  # сопоставляет запросы пользователя с функциями их обработки
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.indexItem, name='detail'),
]
