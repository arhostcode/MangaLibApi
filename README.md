# Unofficial MangaLib (mangalib.me) api
## Quick start

1. Copy or download mangalib_api:
2. Import MangaLibApi to your project:
```python
from mangalib_api import MangaLibApi
```
3. Use MangaLibApi, for example:
```python
from mangalib_api import MangaLibApi

api = MangaLibApi()

list_mangas = api.getMangaList("rate", "desc", 1)
print(list_mangas)

first_manga = api.getManga(id=list_mangas[0]['id'])
print(first_manga)

api.closeApi()
```

## Requires
1. beautifulsoup4
2. selenium
3. chrome and chrome driver


## Simple docs
1. getMangaList()
```python
from mangalib_api import MangaLibApi

api = MangaLibApi()

api.getMangaList("sort", "dir", "page") # return list [ { name: "Manga name", id: "Manga id" } ]

api.closeApi()
```
```
sort:
    (rate, chap_count, name, created_at, views, last_chapter_at)
dir:
    (asc, desc)
page:
    (pageNumber)

```
2. getManga()
```python
from mangalib_api import MangaLibApi

api = MangaLibApi()

api.getManga(name="Manga name") # getting id from mangas.json
api.getManga(id="Manga id")

api.closeApi()
```
Manga class structure:
```
Manga:
    name
    chapterCount
    desc
    rate
    tags
    similar
    imgUrl
    typeM (Манга, Маньхуа, Манхва, Комикс и тп)
```
