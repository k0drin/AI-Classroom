from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoomViewSet, StudentRoomViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'student-rooms', StudentRoomViewSet)

urlpatterns = router.urls

