from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_product, name="durags"),
    path('add/<int:id>/', views.add_to_basket, name="add_to_basket"),
]
