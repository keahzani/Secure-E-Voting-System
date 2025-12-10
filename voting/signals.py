from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vote
from audit.models import AuditLog

@receiver(post_save, sender=Vote)
def log_vote(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action='vote',
            user=instance.voter,
            details=f"Voted for {instance.candidate.name} in {instance.election.title}"
        )

