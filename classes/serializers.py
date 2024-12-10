from rest_framework import serializers
from .models import User, Room, StudentRoom

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class RoomSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'description', 'created_by', 'created_at']

class StudentRoomSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = StudentRoom
        fields = ['id', 'student', 'room', 'joined_at']

