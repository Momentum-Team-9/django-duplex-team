from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Flashcard, Deck

# Create your views here.
def index(request):
    return render(request, "flashcard/index.html")

def list_all_decks(request):
    decks = Deck.objects.all().order_by("title")
    return render(request, "flashcard/list_all_decks.html", {"decks": decks})

def list_all_cards(request):
    cards = Flashcard.objects.all()
    return render(request, "flashcard/list_all_cards.html", {"cards": cards})



