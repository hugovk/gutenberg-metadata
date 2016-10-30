"""
Extract the metadata from Project Gutenberg titles using Gutenberg:
https://github.com/c-w/Gutenberg
Tested on Python 2.7.
"""
# https://github.com/c-w/Gutenberg#installation
from gutenberg.query import get_metadata

import json
import sys


# http://stackoverflow.com/a/652284/724176
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def frozenhack(metadata):
    """Workaround for https://github.com/c-w/Gutenberg/issues/22
    get_metadata('author', 2701) returns frozenset([u'Melville, Hermann'])
    instead of 'Melville, Hermann'.
    """
    try:
        return list(metadata)[0]
    except IndexError:
        return None

metadata = AutoVivification()
i = 0

# Set this magic number to ID of the latest released book:
# https://www.gutenberg.org/ebooks/search/%3Fsort_order%3Drelease_date

# while(i <= 10):  # For testing
while(i <= 53404):
    if i % 100 == 0:
        sys.stdout.write(str(i) + "\r")
    metadata[i]['title'] = frozenhack(get_metadata('title', i))
    metadata[i]['author'] = frozenhack(get_metadata('author', i))
    i += 1
sys.stdout.write("\r\n")

# from pprint import pprint
# pprint(metadata)


with open('gutenberg-metadata.json', 'w') as fp:
    json.dump(metadata, fp, sort_keys=True, indent=2)
