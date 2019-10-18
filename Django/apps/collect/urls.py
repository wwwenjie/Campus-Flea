from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.search, name="cart")
]
