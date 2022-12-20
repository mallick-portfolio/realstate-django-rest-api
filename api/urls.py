from django.contrib import admin
from django.urls import path, include
from contact.views import ContactAPIView
from realtor.views import AgentListAPIView, AgentDetailAPIView, TopSellerListAPIView


urlpatterns = [
    path('contact/', ContactAPIView.as_view(), name="contact"),
    path('agent/', AgentListAPIView.as_view(), name="agents"),
    path('<pk>/', AgentDetailAPIView.as_view(), name="agents"),
    path('agent/top-seller/', TopSellerListAPIView.as_view(), name="agents"),

]
