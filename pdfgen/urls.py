from django.urls import path, include

from pdfgen import views

app_name = 'pdfgen'
urlpatterns = [
    path('', views.PdfGeneratorView.as_view(), name='pdfgenerator'),
]