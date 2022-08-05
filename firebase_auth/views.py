from django.shortcuts import render
from django.contrib.auth import authenticate
from typing import Dict, Tuple
from django.db import IntegrityError
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from users.models import User
from firebase_admin import auth
from firebase_auth.serializers import FireBaseAuthSerializer


# # Create your views here.

class FireBaseAuthRegister(GenericAPIView):
    authentication_classes = []
    serializer_class = FireBaseAuthSerializer
    permission_classes= (permissions.AllowAny,)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class FireBaseAuthLogin(GenericAPIView):
#     authentication_classes = []
#     permission_classes=(permissions.AllowAny,)
#     serializer_class = FireBaseAuthSerializer
    
#     def post(self, request):
#         email= request.data.get('email', None)
#         password= request.data.get('password', None)
        
#         user= authenticate(username=email, password=password)
        
#         if user:
#             serializer = self.serializer_class(user)
            
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({'message':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)    
    
    
    


class FireBaseAuthAPI(GenericAPIView):
    serializer_class = FireBaseAuthSerializer
    permission_classes = []
    
    def post(
        self: "FireBaseAuthAPI",
        request: Request,
        *args: Tuple,
        **kwargs: Dict
    ) -> Response:
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            id_token = serializer.data.get('token')
            
            try: 
                decoded_token = auth.verify_id_token(id_token)
                
            except Exception:
                raise APIException(
                    detail= 'Invalid token',
                    code=status.HTTP_400_BAD_REQUEST
                )
            try:
                firebase_user_id = decoded_token['uid']
            except KeyError:
                raise APIException(
                    detail='No such User',
                    code=status.HTTP_400_BAD_REQUEST
                )
            try:
                user = User.objects.get(firebase_user_id=firebase_user_id)
                content = {
                    "username" :user.email,
                    "email" : user.email,
                    "firebase_user_id" : user.firebase_user_id
                }
                return Response(content, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = auth.get_user(firebase_user_id)
                
                try:
                    new_user = User.objects.create(
                        email= user.email,
                        firebase_user_id= firebase_user_id,
                    )
                    content = {
                        "email":new_user.email,
                        "firebase_user_id": new_user.firebase_user_id
                    }
                    return Response(content, status=status.HTTP_201_CREATED)
                except IntegrityError:
                    raise APIException(
                        detail='User already exists',
                        code=status.HTTP_400_BAD_REQUEST
                    )
                    


@api_view()
def public(request: Request) -> Response:
    return Response({"message": "Hello, User X"})
    
@api_view()
@permission_classes([permissions.IsAuthenticated])
def protected(request: Request) -> Response:
    return Response({"message": f"Hello, {request.user}"})     

