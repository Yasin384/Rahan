from django.db import models

# Create your models here.

class UserScore(models.Model):
    username = models.CharField(max_length=100)
    xp_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.xp_points} XP"

    class Meta:
        ordering = ['-xp_points']
