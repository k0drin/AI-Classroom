from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, Room, StudentRoom
from .serializers import UserSerializer, RoomSerializer, StudentRoomSerializer

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Room ViewSet
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# StudentRoom ViewSet
class StudentRoomViewSet(viewsets.ModelViewSet):
    queryset = StudentRoom.objects.all()
    serializer_class = StudentRoomSerializer

