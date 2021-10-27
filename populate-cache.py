#!/usr/bin/env python
"""
Populate the gutenberg cache
From https://github.com/c-w/gutenberg#looking-up-meta-data
"""
from gutenberg.acquire import get_metadata_cache

print("Warning: this is slow...")
cache = get_metadata_cache()
cache.populate()
