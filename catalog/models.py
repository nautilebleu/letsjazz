from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    is_band = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.name
