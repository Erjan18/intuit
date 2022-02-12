from django.contrib import admin
from .models import *

admin.site.register([Magistracy,Forms_training,Catalog,Description,Oplata_za,Discount,Jobmagis,Enactus,Availability,
                     Transfer])