from django.urls import path
from . import views

app_name = 'developments'

urlpatterns = [
    path('theme/<int:id>', views.theme)
]
