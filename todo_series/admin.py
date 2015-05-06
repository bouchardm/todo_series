from django.contrib import admin

# Register your models here.
from .models import Movie, Episode, Saison

class SaisonInline(admin.TabularInline):
    model = Saison
    extra = 0

class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'imdb_id']
    inlines = [SaisonInline]

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 0

class SaisonAdmin(admin.ModelAdmin):
    fields = ['saison_number']
    inlines = [EpisodeInline]

class EpisodeAdmin(admin.ModelAdmin):
    fields = ['episode_name', 'seen', 'release_date']
    list_display = ['name', 'isSeen', 'isReleased']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Saison, SaisonAdmin)
admin.site.register(Episode, EpisodeAdmin)