# coding=utf-8
from time import timezone
from datetime import date, datetime
from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from lxml import html
import requests

class Movie(models.Model):
    imdb_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default='No title', blank=True)

    def __str__(self):
        return self.title

class Saison(models.Model):
    saison_number = models.IntegerField(default=0)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.movie.title + ' - Saison ' + str(self.saison_number)

class Episode(models.Model):
    saison = models.ForeignKey(Saison)
    episode_name = models.CharField(max_length=200)
    seen = models.BooleanField(default=False)
    release_date = models.DateField(null=True)

    def __str__(self):
        return self.saison.movie.title + ' - Saison ' + str(self.saison.saison_number) + ' - Episode ' + self.episode_name

    def name(self):
        return self.__str__()

    def isSeen(self):
        return self.seen

    isSeen.boolean = True
    isSeen.short_description = "Vue?"

    def isReleased(self):
        if self.release_date is None:
            return False
        else:
            return self.release_date <= date.today()

    isReleased.admin_order_field = 'release_date'
    isReleased.boolean = True
    isReleased.short_description = 'Est sortie?'

@receiver(post_save, sender=Movie)
def update_serie(sender, instance, **kwargs):
    serie_id = instance.imdb_id

    page = requests.get('http://www.imdb.com/title/' + serie_id)
    tree = html.fromstring(page.text)

    saison_list = tree.xpath('//*[@id="title-episode-widget"]/div/div[3]/a/text()')

    for saison in saison_list:
        if str(saison).isdigit():

            new_saison = Saison.objects.get(movie=instance, saison_number=saison)
            if new_saison is None:
                new_saison = Saison(movie=instance, saison_number=saison)
                new_saison.save()

            page = requests.get('http://www.imdb.com/title/' + serie_id + '/episodes?season=' + saison)
            tree = html.fromstring(page.text)
            episode_list_name = tree.xpath('//*[@itemprop="episodes"]/strong[1]/a/text()')
            episode_list_date = tree.xpath('//*[@itemprop="episodes"]/div[1]/text()')

            for name, date in zip(episode_list_name, episode_list_date):
                release_date = None
                try:
                    release_date = datetime.strptime(date.strip(), '%d %b. %Y')
                except ValueError:
                    pass

                try:
                    release_date = datetime.strptime(date.strip(), '%d %b. %Y')
                except ValueError:
                    pass

                episodes = Episode.objects.filter(saison=new_saison, episode_name=name);
                if episodes.__len__() == 0:
                    episode = Episode(saison=new_saison, episode_name=name)
                else:
                    episode = episodes[0]
                    episode.release_date = release_date

                episode.save()
