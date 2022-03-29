
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin123/', admin.site.urls),
    path('', include('appthree.urls', namespace='orders')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
