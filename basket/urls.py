from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.view_basket, name='basket'),
    path('add/<durag_id>/', views.add_to_basket, name='add_to_basket'),
    path('update/<durag_id>/', views.update_basket, name='update_basket'),
    path('delete/<durag_id>/', views.delete_basket, name='delete_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
