from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from contact.models import Contact
from contact.serializers import ContactSerializer
from rest_framework.response import Response
# Create your views here.

class ContactAPIView(APIView):
    def get(self, request, format=None):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response({
            "status": "success",
            'message': "Successfully get contacts",
            "error": False,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "status": "success",
            'message': "Successfully add contact",
            "error": False,
            "data": serializer.data
        },status=status.HTTP_201_CREATED)

        return Response({
            "status": "fail",
            'message': "Failed to add contact",
            "error": serializer.errors,
            "data": False
        }, status=status.HTTP_401_UNAUTHORIZED)
