from django.contrib.auth.models import AbstractUser
from django.db import models

# User Model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# Room Model
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_rooms")
    created_at = models.DateTimeField(auto_now_add=True)

# Many-to-Many Relationship for Students and Rooms
class StudentRoom(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms_joined")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="students")
    joined_at = models.DateTimeField(auto_now_add=True)

