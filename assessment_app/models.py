from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone
from datetime import timedelta



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user.username} - {self.department}"


class EmailVerification(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

    def __str__(self):
        return f"{self.email} - {self.code}"


class UserProgress(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    expertise_field = models.CharField(max_length=100, default='Computer Science')

    # IRT adaptive scoring
    current_step    = models.IntegerField(default=1)
    current_theta   = models.FloatField(default=0.0)
    is_completed    = models.BooleanField(default=False)

    # Batch question cache — stores JSON list of 10 questions
    question_batch  = models.TextField(null=True, blank=True)
    batch_index     = models.IntegerField(default=0)

    # Tracks topics already asked to prevent repetition
    asked_topics    = models.TextField(null=True, blank=True)

    started_at      = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.expertise_field} - Step {self.current_step}"



class AssessmentResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_category = models.CharField(max_length=100)
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.skill_category} - {self.score}"

class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department      = models.CharField(max_length=150)
    expertise_field = models.CharField(max_length=100, default='Full Stack Developer')

    def __str__(self):
        return f"{self.user.username} - {self.department} - {self.expertise_field}"
