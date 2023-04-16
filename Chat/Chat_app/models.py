from django.db import models
from django.contrib.auth.models import User

# class TestUser(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     # email = models.EmailField(max_length=200)
#     # image = models.FileField(null=True, blank=True, upload_to='extra/media/')
#     # user= models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.username
#     class Meta:
#         db_table="user"

class Messages(models.Model):
    message=models.CharField(max_length=500)

    
    def __str__(self):
        return self.message
    
    class Meta:
        db_table='app_Chat'

# Create your models here.
