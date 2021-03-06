from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager, User
from django.db.models.expressions import Value
class Snippet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='snippets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    class Meta:
        ordering = ['created']
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.user.user_name} Profile'

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, address, **extra_fields):
        if not email:
            raise ValueError("email must be provided")
        if not password:
            raise ValueError('password is not provided')
        user = self.model(
            email = self.normalize_email(email), 
            first_name = first_name,
            last_name = last_name,
            address = address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password, first_name, last_name, address, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, address, **extra_fields)
    def create_superuser(self, email, password, first_name, last_name, address, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, address, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
    #abstractuser  has pasword, last_login, is_active by default
    email = models.EmailField(unique = True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=250)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'address']
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

