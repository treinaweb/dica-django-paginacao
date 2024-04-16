from django.contrib import admin
from django.urls import path

from clients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ClientList.as_view()),
]
