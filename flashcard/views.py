from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Flashcard, Deck
from .forms import DeckForm, CardForm

# Create your views here.
def index(request):
    return render(request, "flashcard/index.html")

def list_all_decks(request):
    decks = Deck.objects.all().order_by("title")
    return render(request, "flashcard/list_all_decks.html", {"decks": decks})

def list_all_cards(request):
    cards = Flashcard.objects.all()
    return render(request, "flashcard/list_all_cards.html", {"cards": cards})

def view_deck(request, pk):
    deck = get_object_or_404(Deck, id=pk)
    return render(request, "flashcard/view_deck.html", {"deck": deck})

def create_deck(request):
    if request.method == "POST":
        form = DeckForm(data=request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect("view_deck", pk=deck.pk)
    else:
        form = DeckForm()
    body = {"form": form}
    return render(request, "flashcard/create_deck.html", body)

def create_card(request):
    if request.method == "POST":
        form = CardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect("view_deck", pk=card.pk)
    else:
        form = CardForm()
    body = {"form": form}
    return render(request, "flashcard/create_card.html", body)
    




