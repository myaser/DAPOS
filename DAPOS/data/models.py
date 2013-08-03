from django.db import models
import caching.base
from DAPOS.data.fields import RegexPatternField


class AlkhalilSuffix(caching.base.CachingMixin, models.Model):

    voweled = models.CharField(max_length=6)
    unvoweled = models.CharField(max_length=6)
    description = models.TextField()
    type = models.CharField(max_length=2)
    pattern = RegexPatternField(unique=True)

    objects = caching.base.CachingManager()


class AlkhalilPrefix(caching.base.CachingMixin, models.Model):

    voweled = models.CharField(max_length=6)
    unvoweled = models.CharField(max_length=6)
    description = models.TextField()
    type = models.CharField(max_length=2)
    pattern = RegexPatternField(unique=True)

    objects = caching.base.CachingManager()


# class Tweets(models.Model):
#     # User ID,User name,User influence,Tweet text,Tweet ID,Posting date,Retweets,Hash tags,Mentions,Links
#     pass
