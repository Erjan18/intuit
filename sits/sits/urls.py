from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abiturient/', include('abiturient.urls')),
    path('aspirantura/', include('aspirantura.urls')),
    path('bachelor/', include('bachelor.urls')),
    path('commission/',include('commission.urls')),
    path('magistracy/',include('magistracy.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
