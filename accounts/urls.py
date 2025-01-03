# accounts/urls.py
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', logout_view, name='logout')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
