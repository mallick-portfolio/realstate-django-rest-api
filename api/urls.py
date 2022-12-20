from django.contrib import admin
from django.urls import path, include
from contact.views import ContactAPIView

urlpatterns = [
    path('contact/', ContactAPIView.as_view()),

]
