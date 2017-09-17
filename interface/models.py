from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count, Sum
from django.core.urlresolvers import reverse
from django.db.models.functions import Coalesce
import datetime
from random import randint

class Card(models.Model):
    balance = models.IntegerField(default=0)
    
class FakeCard(models.Model):
    cash = models.IntegerField(default=0)

class ProfileManager(models.Manager):
    def get_by_profile(self, profile):
        return self.get_queryset().filter(profiles=profile)#prefetch_related('profiles')
       
    def get_profiles_by_id(self, user_id):
        # print('a')
        # print(user_id)
        profile = self.get_queryset().get(user_id=user_id)
        # print(profile.id)
        res = self.get_by_profile(profile)
        return self.get_by_profile(profile)

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

class TransactionManager(models.Manager):
    def generate_transaction(self, transaction, user_id):
        trans_id = randint(1, 100)
        # try:
        transaction_sum = int(transaction['TransactionSum'])
        # except ValueError:
          # raise  
        print(transaction_sum)
        print(trans_id)
        print(self.get_queryset().filter(id = trans_id).count() == 0)
        if transaction_sum < 0 and self.get_queryset().filter(id = trans_id).count() == 0:
            tempTransaction =  Transaction()
            tempTransaction.transactionId = trans_id
            tempTransaction.owner = Profile.objects.filter(user_id = user_id)[0]
            tempTransaction.visibility = False
            tempTransaction.save()

    def get_by_userid(self, user_id):
        print(user_id)
        profile = Profile.objects.all().get(user_id=user_id)
        print(profile.id)
        return self.get_queryset().filter(owner=profile)

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
    owner = models.ForeignKey(Profile)
    transaction_company = models.CharField(default='', max_length=50)
    visibility = models.BooleanField(default=False)

    objects = TransactionManager()
