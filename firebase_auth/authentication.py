from logging import raiseExceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions, status
from firebase_admin import auth
from users.models import User
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate('ttlines2-firebaseEnv.json')

default_app = firebase_admin.initialize_app(cred)


class NoAuthToken(exceptions.APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "No authentication token provided"
    default_code = "no_auth_token"


class InvalidAuthToken(exceptions.APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid authentication token provided"
    default_code = "invalid_token"


class FirebaseError(exceptions.APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "The user provided with the auth token is not a valid Firebase user, it has no Firebase UID"
    default_code = "no_firebase_uid"



# should validate the credential and return a tuple(user, auth)
# if the credential is validated. otherwise return none
class FirebaseBackend (BaseAuthentication):
    def authenticate(self, request):
        
        auth_header = request.headers.get('Authorization')
        # auth_header = request.META.get('Authorization')
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
        
        if not id_token or not decoded_token:
            return None
        
        try:
            # get unique user ID
            uid = decoded_token("uid")
            # uid = decoded_token.get("uid")
        except Exception:
            return FirebaseError()
        
        # user, created = User.objects.get_or_create(firebase_user_id=uid)
        try: 
            user = User.objects.get(firebase_user_id=uid)
            # user = User.objects.get_or_create(firebase_user_id=uid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        
        return (user, None)




















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
    