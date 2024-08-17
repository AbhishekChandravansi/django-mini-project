from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print('-------------->',self.request.user)
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        # client_id = self.request.data.get('client_id')
        # client = Client.objects.get(id=client_id)
        serializer.save(created_by=self.request.user)
        
    def get_serializer_context(self):
        return {'request': self.request}
    
class ProjectDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    # lookup_field = 'id'

