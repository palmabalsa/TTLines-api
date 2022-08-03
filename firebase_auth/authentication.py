from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions
from firebase_admin import auth
from users.models import User


class FirebaseBackend (BaseAuthentication):
    def authenticate(self, request):
        
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            return None

        try:
            decoded_token = auth.verify_id_token(auth_token)
            uid = decoded_token["uid"]
        except:
            return None
            
        try:
            user = User.objects.get(username=uid)
            return (user, None)
        except:
            return None


# class FirebaseBackend (BaseAuthentication):
#     def authenticate(self, request):
#         auth_token = request.META.get("HTTP_AUTHORIZATION")
        
#         if not auth_token:
#             return None
#             # raise exceptions.AuthenticationFailed('Credentials not provided')
#         id_token = auth_token.split(" ").pop()
#         if not id_token:
#             return None
#             # raise exceptions.AuthenticationFailed('Credentials not provided')

#         try:
#             decoded_token = auth.verify_id_token(id_token)
#         except Exception:
#             raise exceptions.AuthenticationFailed('Invalid Token')
#         try:
#             firebase_user_id= decoded_token['user_id']
#         except KeyError:
#             raise exceptions.AuthenticationFailed("No such User exists")
        
#         try:
#             user = User.objects.get(firebase_user_id=firebase_user_id)
#             return user, None
#         except User.DoesNotExist:
#             return None
    