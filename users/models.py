
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    
    use_in_migrations: True
    
    def create_user(self, email, password, **extra_fields):    
        if not email: 
            raise ValueError(_('Email required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_suepruser=True'))
        return self.create_user(email, password, **extra_fields)
        



class User(AbstractUser, PermissionsMixin):
    # username = None
    firebase_user_id = models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(_('email address'), blank=False, null=False, unique=True)
    
    USERNAME_FIELD: 'email'
    # REQUIRED_FIELDS: []
    
    objects = UserManager()
    
    class Meta:
        verbose_name = "profile"
        verbose_name_plural= "profiles"
    
    def __str__(self: "User") -> str:
        return f"{self.email}"
    
    # def __str__(self):
    #     return self.email


