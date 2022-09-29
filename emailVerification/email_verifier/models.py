from django.db import models

# Create your models here.

class EmailAddresses(models.Model):
    emailAddress = models.CharField(max_length=100)
    exist = models.BooleanField() # Default is False

    def __str__(self) -> str:
        return f'{self.emailAddress} {self.exist}'