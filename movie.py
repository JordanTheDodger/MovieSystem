class Movie:
    def __init__(self,name,genre,watched=False):
        self.name=name
        self.genre=genre
        self.watched=watched

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json(self):
        return {
            'name':self.name,
            'genre':self.genre,
            'watched': self.watched
        }