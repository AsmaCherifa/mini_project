import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()
from audio.models import CharacterSet
# vecu pb de path
allowed_characters =['a', 'A', 'à', 'À', '?', 'â', 'Â', ',', 'b', 'B', '.', 'c', 'C', ';', 'ç', 'Ç', ':', 'd', 'D', '!', 'e', 'E', 'é', 'É', 'è', 'È', 'ê', 'Ê', 'ë', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'î', 'Î', 'ï', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'ô', 'Ô', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'ù', 'û', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', ' ', "'", '-', '?', ';', 'ç', ':', '!', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', '#', '&', ';', "'", ';', 'ç', 'ç', ':', '!', 'è', 'è', 'ê', 'ê', 'ë', 'ë', 'î', 'î', 'ï', 'ï', 'ô', 'ô', 'ù', 'û', 'û']


for char in allowed_characters:
    CharacterSet.objects.create(character=char)


#python manage.py makemigrations
#python manage.py migrate
#python CharacterSet.py
