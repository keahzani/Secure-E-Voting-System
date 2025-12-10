from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('voter', 'Voter'),
        ('officer', 'Election Officer'),
        ('admin', 'Administrator'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='voter')
    identification_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username} Profile"
