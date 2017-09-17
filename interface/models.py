from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count, Sum
from django.core.urlresolvers import reverse
from django.db.models.functions import Coalesce
import datetime

class Card(models.Model):
    balance = models.IntegerField(default=0)
    
class FakeCard(models.Model):
    cash = models.IntegerField(default=0)

class ProfileManager(models.Manager):
    def get_by_profile(self, profile):
        return self.get_queryset().filter(profiles=profile)
  
    def get_or_create(self, user_id):
        profile = self.get_queryset().filter(user_id=user_id)
        if profile.count() > 0:
            return profile[0]
        else:
            profile = Profile()
            fake_card = FakeCard()
            fake_card.save()
            profile.fake_card = fake_card
            print(user_id)
            profile.user = User.objects.get(id=user_id)
            profile.save()
            return profile

class Profile(models.Model):
    user = models.OneToOneField(User)
    interest = models.TextField(max_length=50)
    fake_card = models.OneToOneField(FakeCard)
    profiles = models.ManyToManyField("self")

    def get_fakecard(self):
        return str(self.fake_card)

    objects=ProfileManager()

class MileStone(models.Model):
    card = models.OneToOneField(FakeCard)
    milestone = models.DateTimeField(default=timezone.now() + datetime.timedelta(7))

# class Contact(models.Model):
    # profiles = models.ManyToManyField(Profile)


class Transaction(models.Model):
    transactionId = models.IntegerField(null=False)
    owner = models.OneToOneField(Profile)
    visibility = models.BooleanField(default=False)
