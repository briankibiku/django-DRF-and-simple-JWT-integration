from lib2to3.pgen2 import token
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .tokens import create_jwt_pair_for_user
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request:Request):
        data = request.data


        serialzer = self.serializer_class(data=data)

        if serialzer.is_valid():
            serialzer.save()

            response = {
                "message": "user ceated successfully",
                "data": serialzer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        response ={
            "message":"User with provided email already exists",
            "data": serialzer.errors
        }

        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes=[]

    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            # Token.objects.get_or_create(user=user)[1]
            response = {
                "massage": "Login successful",
                "tokens": tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid username or password"})
    def get(self, request:Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth),           
        }

        return Response(data=content, status=status.HTTP_200_OK)