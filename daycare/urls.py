from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('sitter/create/', views.sitter_create, name='sitter_create'),
    path('baby/create/', views.baby_create, name='baby_create'),
    path('payment/create/', views.payment_create, name='payment_create'),
    path('procurement/create/', views.procurement_create, name='procurement_create'),
]