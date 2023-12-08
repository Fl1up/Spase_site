from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from spase.apps import SpaseConfig
from spase.views import main

app_name = SpaseConfig.name

urlpatterns = [
    path("", main, name="main"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)