
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
import jwt
from django.conf import settings
# Create your models here.
class CustomUserManager(UserManager):
    
    use_in_migrations: True
    
    def _create_user(self, username, email, password, **extra_fields): 
        if not username: 
            raise ValueError(_('Username required'))   
        if not email: 
            raise ValueError(_('Email required'))
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)
        
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(username, email, password, **extra_fields)
    
    
    
class User(AbstractUser, PermissionsMixin):
    firebase_user_id = models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(_('email address'), blank=False, unique=True)
    # email_verified=models.BooleanField(
    #     _('email_verified'),
    #     default=False,
    #     help_text=(
    #         'Designates whether this users email is verified'
    #     ),
    # )
    EMAIL_FIELD: 'email'
    USERNAME_FIELD: 'email'
    # REQUIRED_FIELDS:[]
    
    objects = CustomUserManager()
    
    # class Meta:
    #     verbose_name = "profile"
    #     verbose_name_plural= "profiles"
        
    @property
    def token(self):
        token=jwt.encode(
            {'username': self.username, 'email': self.email, 
             'exp': datetime.now() + timedelta(hours=24)}, 
            settings.SECRET_KEY, algorithm='HS256')
        return token
    
    def __str__(self: "User") -> str:
        return f"{self.email}"


