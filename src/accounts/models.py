from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):

    phone_number = models.CharField(null=True, max_length=50)
    def __str__(self):
        return self.username

    @property
    def full_name(self):
        full_name = "{} {}".format(self.first_name, self.last_name) \
            if self.first_name and self.last_name else \
            "{}".format(self.first_name) if self.first_name \
                else "{}".format(self.last_name) if self.last_name \
                else None
        return full_name