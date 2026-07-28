from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None,degree=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            degree=degree

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,degree=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            degree=degree

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_degree = (
        ("Foundation","foundation"),
        ('Associate','associate'),
        ('Bachelors','bachelors'),
        ('Masters','masters'),
        ('PHD','phd')
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    username = models.CharField(max_length=50,unique=True,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/user',default='image/user/default_user.jpg',null=True,blank=True)
    degree = models.CharField(choices=user_degree,null=True)
    objects = MyUserManager()

    def show_image(self):
        if self.image:
            return format_html('<image src="{}" width="30px" height="30px">', self.image.url)
        return 'NO image'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app app_label?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin