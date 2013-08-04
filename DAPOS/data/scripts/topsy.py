import os
import csv

from django.template.loader import render_to_string

from DAPOS import PROJECT_ROOT

TOPSY_SCRAP_DIR = '/media/my_files/data/Rania/topsyOutput/'

FIXTURE_DIR = os.path.join(PROJECT_ROOT, 'data/fixtures')


def get_csv_file():
    for path, dirlist, filelist in os.walk(TOPSY_SCRAP_DIR):
        for mfile in filelist:
            with open(path + mfile, 'rb') as csvfile:
                csvfile.readline()
                tweets_generator = csv.reader(csvfile,
                                              delimiter=',', quotechar='"')
                yield mfile.strip("topsySscrap.txt"), tweets_generator


if __name__ == '__main__':
    index = 1
    for num, csvfile in get_csv_file():
        xml_file_name = FIXTURE_DIR + '/tweets_{n}.xml'.format(n=num)

        tweets_list = list(csvfile)
        tweets = enumerate(tweets_list, start=index)
        index += len(tweets_list)

        rendered = render_to_string('tweets.xml', {'lists': tweets})
        open(xml_file_name, 'w').write(rendered.encode('utf8'))
