from django.urls import path,include
from .views import *

urlpatterns = [
    path('magistracy/',MagistracyView.as_view(),name='bachelor'),
    path('training/',FormstrainingrView.as_view(),name='training'),
    path('catalog/',CatalogView.as_view(),name='catalog'),
    path('oplata/',Oplata_zaView.as_view(),name='oplata'),
    path('discount/',DiscountView.as_view(),name='discount'),
    path('transfer/',TransferView.as_view(),name='transfer'),
    path('avia/',AvailabilityView.as_view(),name='avia'),
    path('job/',JobmagistView.as_view(),name='job'),
    path('enactus/',EnactusView.as_view(),name='enactus'),
    path('description/',DescriptionView.as_view(),name='description'),

]