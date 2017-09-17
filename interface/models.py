from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count, Sum
from django.core.urlresolvers import reverse
from django.db.models.functions import Coalesce
import datetime

class FakeCard(models.Model):
    cash = models.IntegerField(default=0)

class ProfileManager(models.Manager):
    def get_by_profile(self, profile):
        return self.get_queryset().filter(profiles=profile)

class Profile(models.Model):
    user = models.OneToOneField(User)
    interest = models.TextField(max_length=50)
    fake_card = models.OneToOneField(FakeCard)
    profiles = models.ManyToManyField(Profile)

class MileStone(models.Model):
    card = models.OneToOneField(FakeCard)
    milestone = models.DateTimeField(default=timezone.now() + datetime.timedelta(7))

# class Contact(models.Model):
    # profiles = models.ManyToManyField(Profile)



class Transaction(models.Model):
    transactionId = models.IntegerField(null=False)
    owner = models.OneToOneField(Profile)
    visibility = models.BooleanField(default=False)
