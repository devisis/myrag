from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_product, name="products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
