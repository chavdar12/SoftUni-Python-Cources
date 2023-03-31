from django.test import TestCase, Client
from django.urls import reverse

from testing.models import Profile


class ProfileViewsTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_whenNoProfiles_shouldRenderCorrectTemplate(self):
        response = self.test_client.get(reverse('profiles'))
        profiles = response.context['profiles']
        form = response.context['form']
        self.assertTemplateUsed(response, 'testing.html')
        self.assertEqual(0, len(profiles))
        self.assertIsNotNone(form)

    def test_getIndex_when2Profiles_shouldRenderCorrectTemplate(self):
        profiles = (
            Profile(name='d', age='1', egn='1234567891'),
            Profile(name='g', age='2', egn='0234567891'),
        )

        [profile.save() for profile in profiles]

        response = self.test_client.get(reverse('profiles'))
        profiles = response.context['profiles']
        form = response.context['form']
        self.assertTemplateUsed(response, 'testing.html')
        self.assertEqual(2, len(profiles))
        self.assertIsNotNone(form)

    def test_postIndex_whenValidEgn_shouldRedirectToIndex(self):
        egn = '1234567891'
        name = 'Dimo'
        age = 18
        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }

        response = self.test_client.post(reverse('profiles'), data=data)
        self.assertRedirects(response, reverse('profiles'))

    def test_postIndex_whenEgnContainsLetter_shouldRenderIndexAndContainError(self):
        egn = '123456789a'
        name = 'Dimo'
        age = 18
        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }

        response = self.test_client.post(reverse('profiles'), data=data)
        profiles = response.context['profiles']
        form = response.context['form']

        self.assertTemplateUsed(response, 'testing.html')
        self.assertEqual(0, len(profiles))
        self.assertIsNotNone(form)
        self.assertIsNotNone(form.errors['egn'])
