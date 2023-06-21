from django.urls import path
from catalog.views import index, home
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', index),
    path('home/', home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)