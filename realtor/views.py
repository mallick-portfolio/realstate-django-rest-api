from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from realtor.serializers import AgentSerializer
from realtor.models import Agent
class AgentListAPIView(ListAPIView):
    permission_classes= (permissions.AllowAny, )
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None

class AgentDetailAPIView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class TopSellerListAPIView(ListAPIView):
    permission_classes= (permissions.IsAuthenticated, )
    queryset = Agent.objects.filter(top_seller = True)
    serializer_class = AgentSerializer
    pagination_class = None
