from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

urlpatterns = [
    # Admin url
    path('admin/', admin.site.urls),
    # API url
    path('api/', include('classes.urls')),
    #JWT urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

