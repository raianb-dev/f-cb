# servidor/urls.py

from django.contrib import admin
from django.urls import path
from homework import views
from login import views as views_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views_login.index, name='login'),
    path('', views.painel, name="painel"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
