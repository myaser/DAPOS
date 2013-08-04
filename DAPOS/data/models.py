from django.db import models
import caching.base
from DAPOS.data.fields import ListField


class AlkhalilSuffix(caching.base.CachingMixin, models.Model):

    voweled = models.CharField(max_length=6)
    unvoweled = models.CharField(max_length=6)
    description = models.TextField()
    type = models.CharField(max_length=2)

    objects = caching.base.CachingManager()

    def __unicode__(self):
        return self.description


class AlkhalilPrefix(caching.base.CachingMixin, models.Model):

    voweled = models.CharField(max_length=6)
    unvoweled = models.CharField(max_length=6)
    description = models.TextField()
    type = models.CharField(max_length=2)

    objects = caching.base.CachingManager()

    def __unicode__(self):
        return self.description


class Tweets(models.Model):
    INFLUENCE_CHOICES = (
        ('HF', 'highly influential'),
        ('MF', 'influential'),
        ('LF', ''),
    )

    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    influence = models.CharField(max_length=50, choices=INFLUENCE_CHOICES)
    tweet_text = models.TextField()
    tweet_id = models.URLField(unique=True)
    posting_date = models.DateField()
    retweets = models.IntegerField()
    hash_tags = ListField()
    mentions = ListField()
    links = ListField()

    def __unicode__(self):
        return self.tweet_text
