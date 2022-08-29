from django.test import TestCase
from .models import Donkey
from django.contrib.auth import get_user_model


# Create your tests here.
class DonkeyTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        test_donkey = Donkey.objects.create(name="Donkey Kong", owner=testuser1, temperament="Is donkey")
        test_donkey.save()

    def test_donkeys_model(self):
        donkey = Donkey.objects.get(id=1)
        actual_owner = str(donkey.owner)
        actual_name = str(donkey.name)
        actual_temperament = str(donkey.temperament)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Donkey Kong")
        self.assertEqual(actual_temperament, "Is donkey")
