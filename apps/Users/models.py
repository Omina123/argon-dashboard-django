from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.core.validators import RegexValidator
#from .managers import CustomUserManager  # Make sure to import your CustomUserManager


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class CustomUserManager(BaseUserManager):

    def create_user(self, email, phone_number=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model( 
            email=self.normalize_email(email),
            phone_number = phone_number, username=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password,phone_number):
        user = self.create_user( email,  password=password,phone_number=phone_number)
        user.is_superuser = True
        user.is_staff =True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

   # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    #gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_organization_staff = models.BooleanField(default=False)
    is_ict_admin = models.BooleanField(default=False, verbose_name="ICT Admin")
    is_Student = models.BooleanField(default=False)
    is_lecture = models.BooleanField(default=False)


    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
