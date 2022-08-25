from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.view_product, name="durags"),
    path('create/', views.AddProductView.as_view(), name='create_product'),
]
