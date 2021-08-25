"""django_duplex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flashcard import views as flashcard_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", flashcard_views.index, name="index"),
    path("home/", flashcard_views.list_all_decks, name="list_all_decks"),
    path("cards/", flashcard_views.list_all_cards, name="list_all_cards"),
    path("play/<int:pk>/", flashcard_views.play_deck, name="play_deck"),
    path("deck/create/", flashcard_views.create_deck, name="create_deck"),
    path("card/create/", flashcard_views.create_card, name="create_card"),
    path("deck/<int:pk>/", flashcard_views.view_deck, name="view_deck"),
    path('accounts/', include('registration.backends.simple.urls')),
]
