from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'home/', views.index, name="home"),
]
+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)