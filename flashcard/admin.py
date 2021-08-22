from django.contrib import admin
from .models import Flashcard, Deck, User
# Register your models here.
admin.site.register(User)
admin.site.register(Deck)
admin.site.register(Flashcard)
