#!/usr/bin/env python
# encoding: utf-8
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


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, frozenset):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


metadata = AutoVivification()
i = 1  # First ebook starts at 1


# Set this magic number to ID of the latest released book:
# https://www.gutenberg.org/ebooks/search/%3Fsort_order%3Drelease_date

# while(i <= 100):  # For testing
while(i <= 53404):
    if i % 100 == 0:
        sys.stdout.write(str(i) + "\r")
    for feature_name in ['author', 'formaturi', 'language', 'rights',
                         'subject', 'title']:
        data = get_metadata(feature_name, i)
        metadata[i][feature_name] = data

    i += 1
sys.stdout.write("\r\n")

# from pprint import pprint
# pprint(metadata)


with open('gutenberg-metadata.json', 'w') as fp:
    json.dump(metadata, fp, cls=SetEncoder, indent=0, separators=(',', ':'),
              sort_keys=True)
