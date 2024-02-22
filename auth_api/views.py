from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
# Create your views here.


class Signup(APIView):
    def post(self, request):
        serlizer = UserSerializer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data)
        return Response(serlizer.errors)


class Login(APIView):
    def post(self, request):
        serlizer = UserSerializer(data=request.data)
        if serlizer.is_valid():
            user = User.objects.get(email=serlizer.data['email'])
            if user:
                password = user.password
                if(password==serlizer.data['password']):
                    return Response({'status':"sucess"})
        return Response({'status':"failed"})