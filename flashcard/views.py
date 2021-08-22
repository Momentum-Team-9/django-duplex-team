from django.shortcuts import render
from .models import User, Flashcard, Deck

# Create your views here.
def play_deck(request):
    decks = Deck.objects.all()
    return render(request, "flashcard/play_deck.html", {"decks": decks})

def create_deck(request):
    decks = Deck.objects.all()
    return render(request, "flashcard/create_deck.html", {"decks": decks})

def index(request):
    return render(request, "flashcard/index.html")