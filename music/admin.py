from django.contrib import admin
from .models import *


class AlbumAdmin(admin.ModelAdmin):
    fields = ('album_title','artist','genre','album_logo')

class SongAdmin(admin.ModelAdmin):
    fields = ('album', 'song_title', 'file_type', 'is_favorite')

admin.site.register(Album,AlbumAdmin)
admin.site.register(Song, SongAdmin)
