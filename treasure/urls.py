from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('answer/',views.answer,name='answer'),
    path('lboard/',views.lboard,name="lboard"),
    path('rules/', views.rules, name='rules'),
]