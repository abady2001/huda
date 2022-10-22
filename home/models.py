from distutils.command import upload
from email import message
from django.db import models
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User


# Create your models here.


# class users_info (models.Model):
#     username = models.CharField(max_length=15, null=True)
#     email = models.EmailField(null=True)
#     password = models.CharField(max_length=50, null=True)
#     Pimg = models.URLField(null=True)
#     firstname = models.CharField(max_length=20, null=True)
#     lastname = models.CharField(max_length=20, null=True)
#     phone = models.CharField(null=True, blank=False, max_length=14)
#     # last_login=models.DateField(null=True)
#     auth = models.Manager()


class events_info (models.Model):
    subject = models.CharField(max_length=100)
    speaker = models.CharField(max_length=50)
    img = models.URLField()
    descripion = models.TextField(max_length=300)


class takePart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def username(request):
        u=request.user
        return u
    user = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100)
    descripion = models.TextField(max_length=300)
    document = models.FileField(upload_to='media/', null=True)

class contactUs(models.Model):
    message = models.TextField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    user = models.CharField(max_length=100, null=True)