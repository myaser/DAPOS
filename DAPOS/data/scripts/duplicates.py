import os
from DAPOS.data.models import Tweets
from DAPOS import PROJECT_ROOT
from django.core import serializers

FIXTURE_DIR = os.path.join(PROJECT_ROOT, 'data/fixtures')
tweets = Tweets.objects.all()

seg_length = 1000
tweets_lists = [tweets[x:x + seg_length] for x in range(0, len(tweets), seg_length)]

x = 1
for tweets in tweets_lists:
    file_name = FIXTURE_DIR + "/tweets_{n}.xml".format(n=x)
    with open(file_name, 'w') as _file:
        print x
        serializers.serialize("xml", tweets, stream=_file, indent=4)
    x += 1
