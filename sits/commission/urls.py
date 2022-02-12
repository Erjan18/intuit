from django.urls import path,include
from .views import *

urlpatterns = [
    path('commission/',CommissionView.as_view(),name='commission'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('paragraph/',ParagraphView.as_view(),name='paragraph'),
    path('description/',ParagraphDisView.as_view(),name='description'),
    path('openday/',OpendayView.as_view(),name='openday')
]