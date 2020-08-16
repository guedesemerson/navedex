from rest_framework.generics import GenericAPIView
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
import jwt



class RegisterView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            data = request.data
            email = data.get('email', '')
            password = data.get('password', '')
            object_pass = User.objects.get(email=email)
            user = auth.authenticate(username=object_pass.username, password=password)


            if user:
                auth_token = jwt.encode(
                    {'username': user.username}, str(settings.JWT_SECRET_KEY))

                data = {'email': object_pass.email, 'token': auth_token}

                return Response(data, status=status.HTTP_200_OK)


        except:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
