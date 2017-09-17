from django.test import TestCase
from django.contrib.auth.models import User
from interface.models import Card
from interface.models import FakeCard
from interface.models import Transaction
from interface.models import Profile
from interface.models import ProfileManager
from interface.models import MileStone

class CardTestCase(TestCase):
    def test_default_value(self):
        card_obj = Card.objects.create()
        self.assertEqual(card_obj.balance, 0)

    def test_defined_value(self):
        card_obj = Card.objects.create(balance = 10)
        self.assertEqual(card_obj.balance, 10)


class FakeCardTestCase(TestCase):
    def test_default_value(self):
        fake_card_obj = FakeCard.objects.create()
        self.assertEqual(fake_card_obj.cash, 0)

    def test_defined_value(self):
        fake_card_obj = FakeCard.objects.create(cash = 10)
        self.assertEqual(fake_card_obj.cash, 10)


class TransactionTestCase(TestCase):
    def test_default_value(self):
        fake_card_obj = FakeCard.objects.create()

        user_obj = User()
        user_obj.save()

        owner_profile = Profile.objects.create(user = user_obj, fake_card = fake_card_obj)
        
        transaction_obj = Transaction.objects.create(transactionId = 10213, owner = owner_profile)
        
        self.assertEqual(transaction_obj.transactionId, 10213)
        self.assertEqual(transaction_obj.visibility, False)


    def test_defined_value(self):
        fake_card_obj = FakeCard.objects.create()
        
        user_obj = User()
        user_obj.save()
        
        owner_profile = Profile.objects.create(user = user_obj, fake_card = fake_card_obj)
        
        transaction_obj = Transaction.objects.create(transactionId = 10213, owner = owner_profile, visibility = True)
        
        self.assertEqual(transaction_obj.transactionId, 10213)
        self.assertEqual(transaction_obj.visibility, True)


class MileStoneTestCase(TestCase):
    def test_default_value(self):
        fake_card_obj = FakeCard.objects.create()
        milestone_obj = MileStone.objects.create(card = fake_card_obj)
        
        milestone_card = milestone_obj.card
        
        self.assertEqual(milestone_card.cash, 0)

    def test_defined_value(self):
        fake_card_obj = FakeCard.objects.create(cash = 23)
        milestone_obj = MileStone.objects.create(card = fake_card_obj)
        
        milestone_card = milestone_obj.card
        
        self.assertEqual(milestone_card.cash, 23)


#class ProfileManagerTestCase(TestCase):
#    def test_get_by_profile(self):
#        fake_card_obj = FakeCard.objects.create()
#
#       user_obj = User()
#       user_obj.save()
#
#       owner_profile = Profile(user = user_obj, fake_card = fake_card_obj)
#       owner_profile.save()
#       
#       profile_manager_obj = ProfileManager()
#       profile_manager_obj.get_by_profile(owner_profile)
        #found_profile = profile_manager_obj.get_by_profile(owner_profile)

        #self.assertEqual(found_profile, owner_profile)