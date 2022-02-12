from django.urls import path,include
from .views import *

urlpatterns = [
    path('aspirantura/',AspiranturaView.as_view(),name='aspirantura'),
    path('training/',FormstrainingrView.as_view(),name='training'),
    path('catalog/',CatalogView.as_view(),name='catalog'),
    path('oplata/',Oplata_zaView.as_view(),name='oplata'),
    path('discount/',DiscountView.as_view(),name='discount'),
    path('transfer/',TransferView.as_view(),name='transfer'),
    path('avia/',AvailabilityView.as_view(),name='avia'),
    path('job/',JobspirantView.as_view(),name='job'),
    path('description/',DescriptionView.as_view(),name='description'),

]