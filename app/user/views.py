from rest_framework import generics
from user.serializers import UserSerializer



class CreateUserApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
