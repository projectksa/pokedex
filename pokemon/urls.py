from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name='index_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
