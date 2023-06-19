class Song:
    all = []
    count = len(all)
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_all(self, genre, artist)

    @classmethod
    def add_to_all(cls, song=None, genre=None, artist = None):
        if song is not None:
            cls.all.append(song)
        if genre is not None:
            cls.genres.append(genre)
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        if artist is not None:
            cls.artists.append(artist)
            cls.artist_count[artist] = cls.artist_count.get(artist,0) +1
        cls.count = len(Song.all)

    # def add_to_all(cls, song=None, genre=None):
    # if song is not None:
    #     cls.all.append(song)
    #     cls.count = len(Song.all)
    # if genre is not None:
    #     cls.genres.append(genre)