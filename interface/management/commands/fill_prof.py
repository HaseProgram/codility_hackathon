from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from interface.models import Profile, FakeCard
from faker import Factory
from django.core.files import File
import os
import urllib
from random import choice

class Command(BaseCommand):
    help = 'Fill users'

    def add_arguments(self, parser):
        parser.add_argument('--number',
                action='store',
                dest='number',
                default=10,
                help='Number of users to add'
        )

    def handle(self, *args, **options):
        fake = Factory.create()
        fakeen = Factory.create('en_US')

        number = int(options['number'])
	#imgsc = len(imgs)
        for i in range(0, number):
            profile = fake.simple_profile()

            user = User.objects.create_user(profile['username'], profile['mail'], make_password('qwerty'))
            user.first_name = fakeen.first_name()
            user.last_name = fakeen.last_name()
            user.is_active = True
            user.is_superuser = False
            user.save()

            fake_card = FakeCard()
            fake_card.save()

            profile = Profile()
            profile.user = user
            profile.fake_card = fake_card
            #up.info = '%s [%s]' % (fakeen.company(), fakeen.catch_phrase())
            profile.save()

            self.stdout.write('[%d] added user %s' % (u.id, u.username))


            profile_cnt = randint(1,5)
            for i in range(0, profile_cnt):
                profile = Profile.objects.filter(id=randint(1, Profile_cnt))[0]
                profile.profiles.add(prof)
            self.stdout.write('added profile [%d]' % (profile.id))

