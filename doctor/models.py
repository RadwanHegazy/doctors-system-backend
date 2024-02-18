from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver



class Department (models.Model) : 
    name = models.CharField(max_length=100)

    def __str__(self) : 
        return self.name


class Doctor (AbstractUser):
    username = None
    groups = None
    first_name = None
    last_name = None


    id = models.UUIDField(primary_key=True,editable=False,db_index=True,default=uuid4)
    department = models.ForeignKey(Department,related_name='doc_dep',on_delete=models.SET_NULL,null=True,blank=True)
    picture = models.ImageField(upload_to='pictures/',default='default.png')
    full_name = models.CharField(_('Full Name'),max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(max_length=10000,editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name


    