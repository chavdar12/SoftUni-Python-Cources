from django.core.exceptions import ValidationError
from django.test import TestCase

from testing.forms.profile import ProfileForm
from testing.models import Profile


class TestProfileForm(TestCase):
    def test_ProfileFormSave_shouldBeValid(self):
        egn = '1234567890'
        name = 'Dimo'
        age = 18
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertTrue(form.is_valid())

    def test_ProfileFormSave_shouldBeInvalid(self):
        egn = '123456789a'
        name = 'Dimo'
        age = 18
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())

    def test_ProfileFormSave_shouldBeInvalidWith9Digits(self):
        egn = '123456789'
        name = 'Dimo'
        age = 18
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())

    def test_ProfileFormSave_shouldBeInvalidWith11Digits(self):
        egn = '12345678912'
        name = 'Dimo'
        age = 18
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())
