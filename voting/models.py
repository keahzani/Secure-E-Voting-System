from django.db import models
from django.contrib.auth.models import User
from elections.models import Election, Candidate

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    encrypted_data = models.TextField(blank=True)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'election')  # A user can vote once per election

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.name} in {self.election.title}"
