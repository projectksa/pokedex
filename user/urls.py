from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', user_view, name='user_page'),
    path('login/', login_view, name='login_page'),
    path('register/', register_view, name='register_page'),
    path('logout/', logout_view, name='logout_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
