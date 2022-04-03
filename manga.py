class Manga:
    def __init__(self, name, chapterCount, desc, rate, tags, similar, imgUrl, typeM):
        self.name = name
        self.chapterCount = chapterCount
        self.chapterCount = chapterCount
        self.desc = desc
        self.rate = rate
        self.tags = tags
        self.similar = similar
        self.imgUrl = imgUrl
        self.typeM = typeM
    def __str__(self):
        return f"( Manga: ( name: {self.name}, chapterCount: {self.chapterCount}, desc: {self.desc}, rate: {self.rate}, tags: {self.tags}, similar: {self.similar}, tags: {self.tags}, imgUrl: {self.imgUrl} )"