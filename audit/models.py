from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('vote', 'Vote Cast'),
        ('election_created', 'Election Created'),
        ('vote_tally', 'Vote Tally'),
        ('user_registered', 'User Registered'),
        ('election_edit', 'Election Edited'),
        ('role_change', 'Role Changed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
