from django.core.exceptions import ValidationError
from django.test import TestCase

from testing.models import Profile


class TestProfile(TestCase):
    def test_createProfile_whenValidEgn(self):
        egn = '1234567890'
        name = 'Dimo'
        age = 18
        profile = Profile(
            name=name,
            age=age,
            egn=egn
        )
        profile.full_clean()
        profile.save()

    def test_createProfile_whenInvalidEgn(self):
        egn = '123456789a'
        name = 'Dimo'
        age = 18
        with self.assertRaises(ValidationError) as context:
            profile = Profile(
                name=name,
                age=age,
                egn=egn
            )
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)
