from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.view_product, name="durags"),
    path('details/<int:product_id>/', views.rag_details, name='rag_details'),
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product, name='delete_product'),
]
