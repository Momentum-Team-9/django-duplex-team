from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"
    def __str__(self):
        return self.username

class Deck(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="decks"
    )

    def __str__(self):
        return f'{self.title}'

class Flashcard(models.Model):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name="cards"
    )
    
    def __str__(self):
        return f'{self.question}'