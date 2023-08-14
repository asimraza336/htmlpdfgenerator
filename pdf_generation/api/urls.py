
from django.urls import path
from .views import GeneratePdfView


urlpatterns = [
    path('GeneratePdf/', GeneratePdfView, name='GeneratePdfView')
    
]
