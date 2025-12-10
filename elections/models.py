from django.db import models

class Election(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='candidates')
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.party})"
