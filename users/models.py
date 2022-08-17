
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
import jwt
from django.conf import settings
# Create your models here.
# class CustomUserManager(BaseUserManager):
    
#     use_in_migrations: True
    
#     def _create_user(self, username, email, password, **extra_fields): 
#         if not username: 
#             raise ValueError(_('Username required'))   
#         if not email: 
#             raise ValueError(_('Email required'))
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         user = self.model(email=email, username=username,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_user(self, username, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(username, email, password, **extra_fields)
        
#     def create_superuser(self, username, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
        
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True'))
#         return self.create_user(username, email, password, **extra_fields)


class CustomUserManager(BaseUserManager):
    
    use_in_migrations: True
    
    # def create_user(self, firebase_user_id, email=None, password=None, **extra_fields): 
    def create_user(self, firebase_user_id, **extra_fields): 
        # if not username: 
        #     raise ValueError(_('Username required'))   
        # if not email: 
        #     raise ValueError(_('Email required'))
        # email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        # username = self.model.normalize_username(username)
        user = self.model(firebase_user_id, **extra_fields)
        # user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, firebase_user_id=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        user = self.model(email=email, **extra_fields)
        user.firebase_user_id = firebase_user_id
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    
    
class User(AbstractUser, PermissionsMixin):
    firebase_user_id = models.CharField(primary_key=True, max_length=300, null=False, blank=False, unique=True)
    # email= models.EmailField(_('email address'), blank=False, unique=True)

    # EMAIL_FIELD: 'email'
    # USERNAME_FIELD: 'firebase_user_id'
    # REQUIRED_FIELDS: 'firebase_user_id']
    
    # def __str__(self):
        # return self.firebase_user_id
    objects = CustomUserManager()
    
    def __str__(self: "User") -> str:
        return f"{self.firebase_user_id}"


