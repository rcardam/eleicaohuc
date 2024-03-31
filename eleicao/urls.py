from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("confirma/<str:cpf>", views.confirma, name="confirma"),
    path("votacao", views.votacao, name="votacao"),
    path("confirmavoto/<str:cpf>", views.confirmavoto, name="confirmavoto"),
    path("final", views.final, name="final"),
]