from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from elections.models import Election
from .models import AuditLog

@receiver(post_save, sender=User)
def log_user_role_change(sender, instance, created, **kwargs):
    if not created:
        AuditLog.objects.create(
            action='role_change',
            user=instance,
            description=f'User {instance.username} role changed'
        )

@receiver(post_save, sender=Election)
def log_election_creation(sender, instance, created, **kwargs):
    action = 'election_create' if created else 'election_edit'
    description = f'Election "{instance.title}" created/edited'
    AuditLog.objects.create(
        action=action,
        user=instance.created_by,  # Assuming you have a `created_by` field on Election
        description=description
    )

# Signal for logging vote casting
@receiver(post_save, sender=Vote)
def log_vote_cast(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action='vote',
            user=instance.user,
            description=f'Vote cast by {instance.user.username} for {instance.candidate.name}'
        )

# Signal for logging login/logout actions
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    AuditLog.objects.create(
        action='login',
        user=user,
        description=f'User {user.username} logged in'
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    AuditLog.objects.create(
        action='logout',
        user=user,
        description=f'User {user.username} logged out'
    )
