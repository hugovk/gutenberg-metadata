# gutenberg-metadata

Metadata from Project Gutenberg. For example:

```json
  "1": {
    "author": "United States President (1801-1809)", 
    "formaturi": "http://www.gutenberg.org/ebooks/1.txt.utf-8", 
    "language": "en", 
    "rights": "Public domain in the USA.", 
    "subject": "E201", 
    "title": "The Declaration of Independence of the United States of America"
  }, 
...
  "15": {
    "author": "Melville, Hermann", 
    "formaturi": "http://www.gutenberg.org/files/15/text/moby-117.txt", 
    "language": "en", 
    "rights": "Public domain in the USA.", 
    "subject": "PS", 
    "title": "Moby Dick"
  }, 
```

Uses the [Gutenberg](https://github.com/c-w/Gutenberg) library.

Run `gutenberg-metadata.py` to generate `gutenberg-metadata.json`.
