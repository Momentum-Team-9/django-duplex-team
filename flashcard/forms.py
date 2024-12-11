
from django import forms
from .models import Flashcard, Deck


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title',
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = [
            'question',
            'answer',
            'deck',
        ]