from django.shortcuts import render
from rest_framework import status
from accounts.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Successfully done",
                'error': False,
                'status': 'success',
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
                'message': "Failed to register",
                'error': serializer.errors,
                'status': 'fail',
                "data": False
            }, status=status.HTTP_400_BAD_REQUEST)