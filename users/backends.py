# from users.models import User
# from rest_framework.authentication import BaseAuthentication
# from rest_framework.request import Request
# from rest_framework import exceptions
# from firebase_admin import auth

# from rest_framework.authentication import get_authorization_header
# import jwt
# from django.conf import settings


# class JWTAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         auth_head = get_authorization_header(request)
#         auth_data = auth_head.decode('utf-8')
#         auth_token = auth_data.split(" ")
        
#         if len(auth_token)!= 2:
#             raise exceptions.AuthenticationFailed("Invalid Token")
        
#         token=auth_token[1]
        
#         try:
#             payload=jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

#             username = payload['username']
#             user =User.objects.get(username=username)
            
#             return (user, token)
       
#         except jwt.ExpiredSignatureError as ex:
#             raise exceptions.AuthenticationFailed("Token has expired, login again")
        
#         except jwt.DecodeError as ex:
#             raise exceptions.AuthenticationFailed("Token is Invalid")
        
#         except User.DoesNotExist as no_user:
#             raise exceptions.AuthenticationFailed("No such user exists")
            

# class FirebaseBackend (BaseAuthentication):
#     def authenticate(self, request):
        
#         auth_token = request.headers.get('Authorization')
#         if not auth_token:
#             return None

#         try:
#             decoded_token = auth.verify_id_token(auth_token)
#             uid = decoded_token["uid"]
#         except:
#             return None
            
#         try:
#             user = User.objects.get(username=uid)
#             return (user, None)
#         except:
#             return None


# # class FirebaseBackend (BaseAuthentication):
# #     def authenticate(self, request):
# #         auth_token = request.META.get("HTTP_AUTHORIZATION")
        
# #         if not auth_token:
# #             return None
# #             # raise exceptions.AuthenticationFailed('Credentials not provided')
# #         id_token = auth_token.split(" ").pop()
# #         if not id_token:
# #             return None
# #             # raise exceptions.AuthenticationFailed('Credentials not provided')

# #         try:
# #             decoded_token = auth.verify_id_token(id_token)
# #         except Exception:
# #             raise exceptions.AuthenticationFailed('Invalid Token')
# #         try:
# #             firebase_user_id= decoded_token['user_id']
# #         except KeyError:
# #             raise exceptions.AuthenticationFailed("No such User exists")
        
# #         try:
# #             user = User.objects.get(firebase_user_id=firebase_user_id)
# #             return user, None
# #         except User.DoesNotExist:
# #             return None
    