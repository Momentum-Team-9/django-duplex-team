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
    author = models.CharField(max_length=250)
    deck = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="deck"
    )

    def __str__(self):
        return f'{self.title}, {self.author}'

class Flashcard(models.Model):
    title = models.CharField(max_length=250)
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    flashcard = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name="flashcard"
    )
    
    def __str__(self):
        return f'{self.title}'