from django.urls import path, re_path
from . import views

app_name = "TEST"

urlpatterns = [
    path('hello/<str:name>', views.hello, kwargs={'kilometers': "34"}),
    path('docx/', views.docx),
    path('test/', views.test),
    re_path(r'^', views.start),
]