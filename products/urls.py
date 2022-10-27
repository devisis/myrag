from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.view_product, name="durags"),
    path('create/', views.create_product, name='create_product'),
]
