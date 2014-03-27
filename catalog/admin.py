from django.contrib import admin

from models import Artist, Album

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_band')
    search_fields = ('name',)
    list_filter = ('is_band',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist')
    search_fields = ('name', 'artist__name')
    list_filter = ('artist__is_band',)


# Register your models here.
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
