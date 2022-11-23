
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class CustomUserManager(BaseUserManager):
    
    use_in_migrations: True
    
    # def create_user(self, firebase_user_id, email=None, password=None, **extra_fields): 
    def create_user(self, firebase_user_id, **extra_fields): 
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(firebase_user_id, **extra_fields)

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
    objects = CustomUserManager()
    
    def __str__(self: "User") -> str:
        return f"{self.firebase_user_id}"


