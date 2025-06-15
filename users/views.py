
from rest_framework import generics
from .serializers import RegisterSerializer,CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Create your views here.
