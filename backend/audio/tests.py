import unittest
from .models import Transcription
from django.core.exceptions import ValidationError

class TestTranscription(unittest.TestCase):

    def setUp(self):
        self.validator = Transcription()

    def test_no_numbers_allowed(self):
        self.validator.text = "This has a number 123."
        with self.assertRaises(ValidationError, msg="Numbers are not allowed in transcription text."):
            self.validator.validate_transcription_text()

    def test_capital_letters_rule(self):
        self.validator.text = "Invalid Text"
        with self.assertRaises(ValidationError, msg="Only the first word should be in Capital Letter"):
            self.validator.validate_transcription_text()

    def test_spaces(self):
        self.validator.text = "Too  many  spaces."
        with self.assertRaises(ValidationError, msg="Only zero or one space is allowed between two characters."):
            self.validator.validate_transcription_text()


    def test_punctuation(self):
            self.validator.text = "Invalid punctuation here ?"
            with self.assertRaises(ValidationError, msg="Invalid punctuation at the end of the text."):
                self.validator.validate_transcription_text()

    def test_valid(self):
        self.validator.text = "Valid text"
        self.validator.validate_transcription_text() 

    def test_invalid_punctuation_at_end_rule(self):
            self.validator.text = "Invalid punctuation here ,"
            with self.assertRaises(ValidationError, msg="Invalid punctuation at the end of the text."):
                self.validator.validate_transcription_text()


    def test_invalid_characters_rule(self):
            self.validator.text = "Invalid @ characters!"
            with self.assertRaises(ValidationError, msg="Invalid characters in transcription text: @, !"):
                    self.validator.validate_transcription_text()

#python manage.py test