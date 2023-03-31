from unittest import TestCase

from django.core.exceptions import ValidationError

from testing.validators import contains_only_digits


class ContainsOnlyDigitsValidatorTests(TestCase):
    def test_validator_whenValueContainsOnlyDigits_shouldDoNothing(self):
        contains_only_digits('123')

    def test_validator_whenValueIsEmpty_shouldDoNothing(self):
        contains_only_digits('')

    def test_validator_whenValueContainsLetter_shouldContainError(self):
        with self.assertRaises(ValidationError) as context:
            contains_only_digits('a')

        self.assertIsNotNone(context.exception)
