from django.shortcuts import render

from .models import MusicPlaylist


def index(request):
    Playlist = MusicPlaylist.objects.all()
    context = {'Playlist': Playlist}
    return render(request, 'musicplaylist_app/index.html', context)