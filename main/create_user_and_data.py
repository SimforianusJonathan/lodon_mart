import os
import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Product  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lodon_mart.settings')
django.setup()

class Command(BaseCommand):
    help = 'Create 2 users and 3 dummy mood entries'

    def handle(self, *args, **kwargs):
        # Membuat pengguna
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')

        self.stdout.write(self.style.SUCCESS(f'Successfully created users: {user1.username}, {user2.username}'))

        # Membuat data dummy untuk MoodEntry
        for i in range(0, 3):

        # Jika ingin membuat data mengenai field tiap user yang unik dan tidak berpola, tidak perlu menggunakan for loop dan lakukan sebanyak 3 kali untuk masing-masing user.
            Product.objects.create(
                user=user1,
                name=f"produk lodon user1 ke {i}",
                price=100 * (i+1), # harga produk 1,2,3 = 100, 200, 300
                description=f'Inilah produk ke {i} dari user1'
            )
            Product.objects.create(
                user=user2,
                name=f"produk lodon user2 ke {i}",
                price=200 * (i+1),  # harga produk 1,2,3 = 200, 400, 600
                description=f'Inilah produk ke {i} dari user2'
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully created dummy products data.'))
