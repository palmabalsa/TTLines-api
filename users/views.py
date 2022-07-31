
from typing import Dict, Tuple
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from firebase_admin import auth
from .serializers import RegisterUserSerializer, FireBaseAuthSerializer


# Create your views here.
class FireBaseAuthAPI(GenericAPIView):
    serializer_class = FireBaseAuthSerializer
    
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
                    # "username" :user.username,
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
@permission_classes([IsAuthenticated])
def protected(request: Request) -> Response:
    return Response({"message": f"Hello, {request.user}"})     





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    lookup_field = 'username'
    
class UserRegistration(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            user = reg_serializer.save()
            if user:
                return Response(status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)