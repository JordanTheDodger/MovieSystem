"""'with is a construct that allows to open a file, you can write on it or read from it and it closes automatically.
it also allows to assign file with mode to a variable that can be treated as file variable"""
import os
import json
from user import User


def menu():
    user_name = input('please enter user name: ')

    filename = f'{user_name}.txt'
    if file_exists(filename):
        print(f'Welcome member {user_name}')
        with open(filename, 'r') as usr_file:
            json_data = json.load(usr_file)
        user = User.from_json(json_data)

    else:
        user = User(user_name)
        print(f'Welcome {user_name}')

    user_input = input(
        "Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie watched, 'd' delete a movie, "
        "'l' to see the list of watched movies or 'f' to save and  'q' to  quit ")

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input('enter movie name')
            movie_genre = input('enter movie genre')
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print(f'Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}')
        elif user_input == 'w':
            watched_movie = input('enter the movie name to set as watched')
            user.set_watched(watched_movie)
        elif user_input == 'd':
            delete_movie = input('enter movie name to delete: ')
            user.delete_movie(delete_movie)
        elif user_input == 'l':
            for movie in user.movies:
                print('Name: {} genre:{} worked:{}'.format(movie.name, movie.genre, movie.watched))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input(
            "Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie watched, 'd' delete a movie, "
            "'l' to see the list of watched movies or 'q' to save and quit ")


def file_exists(filename):
    return os.path.isfile(filename)


menu()


