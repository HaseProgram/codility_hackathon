from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count, Sum
from django.core.urlresolvers import reverse
from django.db.models.functions import Coalesce
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User)
    interest = models.TextField(max_length=50)
    fake_card = models.OneToOneField(FakeCard)

class FakeCard(models.Model):
	cash = models.IntegerField(default=0)

class MileStone(models.Model):
	card = models.OneToOneField(FakeCard)
	milestone = models.DateTimeField(deault=timezone.now() + datetime.timedelta(7))

class Friend(models.Model):
	friends = models.ManyToManyField(Profile)

class Transaction(models.Model):
	transactionId = models.IntegerField(null=False)
	owner = models.OneToOneField(Profile)
	visibility = models.BooleanField(default=null)




