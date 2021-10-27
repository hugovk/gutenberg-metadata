# gutenberg-metadata

[![Lint](https://github.com/hugovk/gutenberg-metadata/actions/workflows/lint.yml/badge.svg)](https://github.com/hugovk/gutenberg-metadata/actions/workflows/lint.yml)

Metadata from 60,559 Project Gutenberg ebooks.

## The data

Grab the data from [gutenberg-metadata.json](http://hugovk.github.io/gutenberg-metadata/gutenberg-metadata.json).

## To generate

Uses the [Gutenberg](https://github.com/c-w/Gutenberg) library.

Run `gutenberg-metadata.py` to generate `gutenberg-metadata.json`.

## Sample data

For example:

```json
"1":{
"author":[
"United States President (1801-1809)"
],
"formaturi":[
"http://www.gutenberg.org/ebooks/1.txt.utf-8",
"http://www.gutenberg.org/files/1/1.txt",
"http://www.gutenberg.org/ebooks/1.html.images",
"http://www.gutenberg.org/ebooks/1.html.noimages",
"http://www.gutenberg.org/files/1/1.zip",
"http://www.gutenberg.org/ebooks/1.epub.images",
"http://www.gutenberg.org/ebooks/1.rdf",
"http://www.gutenberg.org/ebooks/1.kindle.noimages",
"http://www.gutenberg.org/6/5/2/6527/6527-t/6527-t.tex",
"http://www.gutenberg.org/ebooks/1.epub.noimages",
"http://www.gutenberg.org/6/5/2/6527/6527-t.zip",
"http://www.gutenberg.org/ebooks/1.kindle.images"
],
"language":[
"en"
],
"rights":[
"Public domain in the USA."
],
"subject":[
"E201",
"United States. Declaration of Independence",
"United States -- History -- Revolution, 1775-1783 -- Sources",
"JK"
],
"title":[
"The Declaration of Independence of the United States of America"
]
},
...
"15":{
"author":[
"Melville, Hermann"
],
"formaturi":[
"http://www.gutenberg.org/files/15/text/moby-117.txt",
"http://www.gutenberg.org/files/15/text/moby-097.txt",
"http://www.gutenberg.org/files/15/text/moby-054.txt",
"http://www.gutenberg.org/files/15/text/moby-041.txt",
"http://www.gutenberg.org/files/15/text/moby-021.txt",
"http://www.gutenberg.org/files/15/text/moby-062.txt",
"http://www.gutenberg.org/files/15/text/moby-056.txt",
"http://www.gutenberg.org/files/15/text/moby-065.txt",
"http://www.gutenberg.org/files/15/text/moby-077.txt",
"http://www.gutenberg.org/files/15/text/moby-006.txt",
"http://www.gutenberg.org/ebooks/15.html.noimages",
"http://www.gutenberg.org/files/15/text/moby-107.txt",
"http://www.gutenberg.org/files/15/text/moby-080.txt",
"http://www.gutenberg.org/files/15/text/moby-119.txt",
"http://www.gutenberg.org/files/15/text/moby-091.txt",
"http://www.gutenberg.org/files/15/text/moby-087.txt",
"http://www.gutenberg.org/files/15/text/moby-001.txt",
"http://www.gutenberg.org/files/15/text/moby-058.txt",
"http://www.gutenberg.org/files/15/text/moby-114.txt",
"http://www.gutenberg.org/files/15/text/moby-003.txt",
"http://www.gutenberg.org/files/15/text/moby-045.txt",
"http://www.gutenberg.org/files/15/text/moby-035.txt",
"http://www.gutenberg.org/ebooks/15.txt.utf-8",
"http://www.gutenberg.org/files/15/text/moby-068.txt",
"http://www.gutenberg.org/files/15/text/moby-079.txt",
"http://www.gutenberg.org/files/15/text/moby-038.txt",
"http://www.gutenberg.org/files/15/text/moby-102.txt",
"http://www.gutenberg.org/files/15/text/moby-051.txt",
"http://www.gutenberg.org/files/15/text/moby-000.txt",
"http://www.gutenberg.org/files/15/text/moby-074.txt",
"http://www.gutenberg.org/files/15/text/moby-026.txt",
"http://www.gutenberg.org/files/15/text/moby-124.txt",
"http://www.gutenberg.org/ebooks/15.epub.images",
"http://www.gutenberg.org/files/15/text/moby-067.txt",
"http://www.gutenberg.org/files/15/text/moby-127.txt",
"http://www.gutenberg.org/files/15/text/moby-076.txt",
"http://www.gutenberg.org/files/15/text/moby-008.txt",
"http://www.gutenberg.org/files/15/text/moby-055.txt",
"http://www.gutenberg.org/files/15/15.txt",
"http://www.gutenberg.org/files/15/text/moby-022.txt",
"http://www.gutenberg.org/files/15/text/moby-095.txt",
"http://www.gutenberg.org/files/15/text/moby-011.txt",
"http://www.gutenberg.org/files/15/text/moby-047.txt",
"http://www.gutenberg.org/files/15/text/moby-090.txt",
"http://www.gutenberg.org/files/15/text/moby-085.txt",
"http://www.gutenberg.org/files/15/15-text.zip",
"http://www.gutenberg.org/files/15/text/moby-092.txt",
"http://www.gutenberg.org/files/15/text/moby-042.txt",
"http://www.gutenberg.org/files/15/text/moby-034.txt",
"http://www.gutenberg.org/files/15/text/moby-075.txt",
"http://www.gutenberg.org/files/15/text/moby-099.txt",
"http://www.gutenberg.org/files/15/text/moby-072.txt",
"http://www.gutenberg.org/files/15/text/moby-100.txt",
"http://www.gutenberg.org/files/15/text/moby-052.txt",
"http://www.gutenberg.org/files/15/text/moby-036.txt",
"http://www.gutenberg.org/files/15/text/moby-071.txt",
"http://www.gutenberg.org/ebooks/15.epub.noimages",
"http://www.gutenberg.org/files/15/text/moby-093.txt",
"http://www.gutenberg.org/files/15/text/moby-049.txt",
"http://www.gutenberg.org/files/15/text/moby-129.txt",
"http://www.gutenberg.org/files/15/text/moby-063.txt",
"http://www.gutenberg.org/files/15/text/moby-112.txt",
"http://www.gutenberg.org/files/15/text/moby-002.txt",
"http://www.gutenberg.org/files/15/text/moby-089.txt",
"http://www.gutenberg.org/files/15/text/moby-059.txt",
"http://www.gutenberg.org/files/15/text/moby-083.txt",
"http://www.gutenberg.org/files/15/text/moby-037.txt",
"http://www.gutenberg.org/files/15/text/moby-109.txt",
"http://www.gutenberg.org/files/15/text/moby-046.txt",
"http://www.gutenberg.org/files/15/text/moby-104.txt",
"http://www.gutenberg.org/files/15/text/moby-094.txt",
"http://www.gutenberg.org/files/15/text/moby-012.txt",
"http://www.gutenberg.org/files/15/text/moby-024.txt",
"http://www.gutenberg.org/files/15/text/moby-018.txt",
"http://www.gutenberg.org/files/15/text/moby-106.txt",
"http://www.gutenberg.org/files/15/text/moby-010.txt",
"http://www.gutenberg.org/files/15/text/moby-118.txt",
"http://www.gutenberg.org/files/15/text/moby-070.txt",
"http://www.gutenberg.org/files/15/text/moby-088.txt",
"http://www.gutenberg.org/files/15/text/moby-132.txt",
"http://www.gutenberg.org/files/15/text/moby-125.txt",
"http://www.gutenberg.org/files/15/text/moby-040.txt",
"http://www.gutenberg.org/files/15/text/moby-020.txt",
"http://www.gutenberg.org/files/15/text/moby-098.txt",
"http://www.gutenberg.org/files/15/text/moby-032.txt",
"http://www.gutenberg.org/files/15/text/moby-064.txt",
"http://www.gutenberg.org/files/15/text/moby-113.txt",
"http://www.gutenberg.org/files/15/text/moby-013.txt",
"http://www.gutenberg.org/files/15/text/moby-048.txt",
"http://www.gutenberg.org/files/15/text/moby-122.txt",
"http://www.gutenberg.org/files/15/text/moby-031.txt",
"http://www.gutenberg.org/files/15/text/moby-014.txt",
"http://www.gutenberg.org/files/15/text/moby-084.txt",
"http://www.gutenberg.org/files/15/text/moby-128.txt",
"http://www.gutenberg.org/files/15/text/moby-078.txt",
"http://www.gutenberg.org/files/15/text/moby-111.txt",
"http://www.gutenberg.org/files/15/text/moby-017.txt",
"http://www.gutenberg.org/files/15/text/moby-120.txt",
"http://www.gutenberg.org/files/15/text/moby-057.txt",
"http://www.gutenberg.org/files/15/text/moby-060.txt",
"http://www.gutenberg.org/files/15/text/moby-009.txt",
"http://www.gutenberg.org/files/15/text/moby-050.txt",
"http://www.gutenberg.org/files/15/text/moby-073.txt",
"http://www.gutenberg.org/ebooks/15.kindle.images",
"http://www.gutenberg.org/files/15/text/moby-110.txt",
"http://www.gutenberg.org/files/15/text/moby-096.txt",
"http://www.gutenberg.org/files/15/text/moby-082.txt",
"http://www.gutenberg.org/files/15/text/moby-025.txt",
"http://www.gutenberg.org/files/15/text/moby-123.txt",
"http://www.gutenberg.org/files/15/text/moby-131.txt",
"http://www.gutenberg.org/files/15/text/moby-101.txt",
"http://www.gutenberg.org/files/15/text/moby-007.txt",
"http://www.gutenberg.org/files/15/text/moby-030.txt",
"http://www.gutenberg.org/files/15/text/moby-004.txt",
"http://www.gutenberg.org/files/15/text/moby-133.txt",
"http://www.gutenberg.org/files/15/text/moby-016.txt",
"http://www.gutenberg.org/files/15/text/moby-044.txt",
"http://www.gutenberg.org/files/15/text/moby-019.txt",
"http://www.gutenberg.org/files/15/text/moby-105.txt",
"http://www.gutenberg.org/files/15/text/moby-043.txt",
"http://www.gutenberg.org/files/15/text/moby-066.txt",
"http://www.gutenberg.org/ebooks/15.kindle.noimages",
"http://www.gutenberg.org/files/15/text/moby-039.txt",
"http://www.gutenberg.org/files/15/text/moby-108.txt",
"http://www.gutenberg.org/files/15/text/moby-115.txt",
"http://www.gutenberg.org/files/15/text/moby-130.txt",
"http://www.gutenberg.org/files/15/text/moby-116.txt",
"http://www.gutenberg.org/files/15/text/moby-033.txt",
"http://www.gutenberg.org/files/15/text/moby-027.txt",
"http://www.gutenberg.org/files/15/text/moby-061.txt",
"http://www.gutenberg.org/files/15/text/moby-126.txt",
"http://www.gutenberg.org/files/15/text/moby-134.txt",
"http://www.gutenberg.org/files/15/text/moby-069.txt",
"http://www.gutenberg.org/files/15/text/moby-028.txt",
"http://www.gutenberg.org/files/15/text/moby-005.txt",
"http://www.gutenberg.org/files/15/text/moby-086.txt",
"http://www.gutenberg.org/files/15/text/moby-121.txt",
"http://www.gutenberg.org/files/15/text/moby-015.txt",
"http://www.gutenberg.org/files/15/text/moby-053.txt",
"http://www.gutenberg.org/files/15/15.zip",
"http://www.gutenberg.org/files/15/text/moby-029.txt",
"http://www.gutenberg.org/files/15/text/moby-081.txt",
"http://www.gutenberg.org/files/15/text/moby-023.txt",
"http://www.gutenberg.org/ebooks/15.rdf",
"http://www.gutenberg.org/ebooks/15.html.images",
"http://www.gutenberg.org/files/15/text/moby-103.txt"
],
"language":[
"en"
],
"rights":[
"Public domain in the USA."
],
"subject":[
"PS",
"Ahab, Captain (Fictitious character) -- Fiction",
"Psychological fiction",
"Ship captains -- Fiction",
"Whaling -- Fiction",
"Whales -- Fiction",
"Mentally ill -- Fiction",
"Whaling ships -- Fiction",
"Sea stories",
"Adventure stories"
],
"title":[
"Moby Dick"
]
},
```
