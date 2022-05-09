from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True, )
    sur_name=models.CharField(max_length=50, blank=True, null=True, )
    age=models.IntegerField(blank=True, null=True, )
    date=models.DateTimeField(auto_now_add=True,)
    last_login=models.DateTimeField(auto_now=True, null=True, ) 
    avatar = models.ImageField(null=True, upload_to="media/")
    def __str__(self):
        return f"{self.name} - {self.age}"

    class Meta:
        ordering =("-age",)

class Teachers(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True, )
    sur_name=models.CharField(max_length=50, blank=True, null=True, )
    age=models.IntegerField(blank=True, null=True, )
    date=models.DateTimeField(auto_now_add=True,)
    last_login=models.DateTimeField(auto_now=True, null=True, ) 
    avatar = models.ImageField(null=True, upload_to="media/")
    reg_login=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.age}"