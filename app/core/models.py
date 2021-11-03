from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class UserManager(BaseUserManager):
    """ Managers creating user new users from command line """

    def create_user(self,email,password=None,**extra_fields):
        
        user = self.model(
            email = email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db) 

        return user


class User(AbstractBaseUser):
    """ Override django user model to use email as username"""

    email = models.EmailField(max_length=100,blank=False,null=False,unique=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=1)
    is_admin = models.BooleanField(default=0)
    is_staff = models.BooleanField(default=0)


    objects = UserManager() 

    USERNAME_FIELD = 'email'
