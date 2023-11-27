from django.db import models
from django.core.exceptions import ValidationError

#table Annotator
class Annotator(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

#table audio
class Audio(models.Model):
    id = models.AutoField(primary_key=True) 
    record_name = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/', default='default_audio.mp3')
    status = models.CharField(max_length=20, default='available') 

#table Transcription
class Transcription(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    annotator = models.ForeignKey(Annotator, on_delete=models.CASCADE)
    text = models.TextField()

    def validate_transcription_text(self):
        #retrieve the set of allowed characters from the CharacterSet model.
        allowed_characters = set(CharacterSet.objects.values_list('character', flat=True))
        transcription = self.text
        # Rule 1 : Numbers are voluntarily excluded
        if any(char.isdigit() for char in transcription):
            raise ValidationError("Numbers are not allowed in transcription text.")

        # Rule 2: Capital letters are allowed only as the first word letter or if all letters in the word are uppercase
        '''for word in self.text.split():
            print(self.text.split())
            # Check if the word is alphabetical and contains at least one letter
            if not word[0].isupper():
                raise ValidationError("Capital letters are allowed only as the first word letter or if all letters in the word are uppercase")
            else:
                print('asma')
'''
        for word in self.text.split():
            print(self.text.split())
            if not word[0].isupper():
                print('asma')
                break #OUT
            raise ValidationError("Capital letters are allowed only as the first word letter or if all letters in the word are uppercase")

        # Rule 3 : There can be only zero or one space between two characters
        if '  ' in transcription:
            raise ValidationError("Only zero or one space is allowed between two characters.")

        # Rule 4 : Characters ?.! should be end of text or followed by one space and an uppercase character
        if transcription.endswith(('?', '!', '.')):
            if transcription[-2] != ' ' and not transcription[-1].isupper():
                raise ValidationError("Invalid punctuation at the end of the text.")

        # Rule 5 : Characters ,;: should be end of text or followed by one space
        if transcription.endswith((',', ';', ':')):
            if transcription[-2] != ' ':
                raise ValidationError("Invalid punctuation at the end of the text.")

        # Rule 6 : Validate characters against the allowed set
        if not set(transcription).issubset(allowed_characters):
            invalid_characters = set(transcription) - allowed_characters
            raise ValidationError(f"Invalid characters in transcription text: {', '.join(invalid_characters)}")

    def save(self, *args, **kwargs):
        self.validate_transcription_text()
        super().save(*args, **kwargs)
   

#allowed character
class CharacterSet(models.Model):
    character = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.username