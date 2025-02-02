from logging import raiseExceptions
from multiprocessing import AuthenticationError
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions, status
from firebase_admin import auth
from users.models import User
from django.contrib.auth import get_user_model

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



class FirebaseBackend(BaseAuthentication):
    def authenticate(self, request):
        
        all_info = request.headers
        # print(all_info)
        
        # recieve auth header 
        auth_header = request.headers.get('Authorization')

        # print ('auth_header = ')
        # print(auth_header)

        if not auth_header:
             raise NoAuthToken("No auth token provided")
         
        id_token = auth_header.split(' ').pop()
        # print ('id_token = ')
        # print (id_token)
        try:
            decoded_token = auth.verify_id_token(id_token)
            # print ('decoded_token = ')
            # print (decoded_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
        
        try:
            uid = decoded_token['uid']
            # print ('uid = ')
            # print (uid)
        except Exception:
             return FirebaseError()

        User = get_user_model()
        fbuserusername = decoded_token['email']
        fbuseremail = decoded_token['email']
      
        user, created = User.objects.get_or_create(firebase_user_id=uid, username=fbuserusername, email=fbuseremail)

        return (user, None)