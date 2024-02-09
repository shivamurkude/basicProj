from django.db import models

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)


    def __str__(self) -> str:
        return self.email