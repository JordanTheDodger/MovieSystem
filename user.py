from typing import List, Any

from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):  # my_user_object.add_movie(name,genre)
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        # if name of the movie is not equal to then lambda function keeps it
        # if it is finds an equal movie name then it deletes it
        self.movies = list(filter(lambda x: x.name != name, self.movies))

    def watched_movies(self):
        # most thinked  way
        # watched_movies_watched=[]
        # for movie in self.movies:
        #     if movie.watched==True:
        #         watched_movies_watched.append(movie.name)
        #
        # return watched_movies_watched

        # using filter method
        # lamba is jsut lika a function, does not have a name so it can't define and call it
        # here it takes x  where x is all elements in x.movies and
        # return "true" if x.watched is true and "false if x.watched is false
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched

    # "Json" is essentially a python dictionary that can have lists in it
    # it gives a dicitonary representation
    def json(self):

        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies  # list comprehenshion
                #naturally movie.json does not exist so we have to create a json method in movie.py
            ]
        }

    # loading data from JSON files
    # @classmethod
    # def from_json(cls, json_data):
    #     usr_json = User(json_data['name'])
    #     usr_movies: List[Any] = []
    #     for usermovies in json_data['movies']:  # usermmovies becomes a dictionary as json_data['movies'] is a dictionary that has name,genre,watched
    #         ''''' error spotted'''# usr_movies.append(usermmovies) # this can not be written coz it will copy name of the user as well. We are interested in only movie's name,genre,watched
    #         usr_movies.append(Movie(usermovies['name'], usermovies['genre'], usermovies['watched'])) # coz we want only movie's name,genre,watched. i.e we have to access from ther dictionary
    #     usr_json.movies = usermovies
    #
    #     return usr_json

    '''Reading and Storing data in CSV'''
    # reading and storing data in CSV format

    # def save_to_file(self):
    #     # saving data to a file using csv format comma separated format
    #     with open("{}.txt".format(self.name),'w') as f:
    #         f.write(self.name + "\n") # user's name
    #         # watched is boolean so we have to convert it to string
    #         for movielsit in self.movies:
    #             f.write('{},{},{} \n'.format(movielsit.name, movielsit.genre, str(movielsit.watched)))
    #
    # @classmethod
    # def load_from_file(cls,filename):
    #     with open(filename,'r') as file:
    #         content = file.readlines() # return a list of all contents on the file
    #         username = content[0]
    #         movies_load_from_file = []
    #         # we need to split in three pieces movie name,genre,watched so we can append it to list
    #         #then pass it to when we are calling Movie() in below for loop
    #
    #         # username is not stored as list so if we start reading from content[0] then we will get erro so wen need to start from content[1] as it is a list of moviename,genre,watched. to achieve this we will ise "SLICING"
    #         for line in content[1:]:
    #             movie_data=line.split(',') #['name','movie','genre']
    #             # when we write to a file we are writing string to a file or  literal character to a file
    #             # so when we load the file 'false' will be string false not boolean
    #             # and this is why writing movie_data[2]=='True' will give us a boolean value
    #             # movie_data[2]=='True if "watched" is "True" then we wil get True or else we will get False if it is False
    #             movies_load_from_file.append(Movie(movie_data[0],movie_data[1],movie_data[2]=='True'))   # movie_data[2] will store watched boolean value, so if we write movie_data[2] it will store string 'true' or 'false'
    #
    #
    #
    #     user =cls(username)
    #     user.movies=movies_load_from_file
    #     return user
