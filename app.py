# "with" is a construct that allows to open a file, you can write on it or read from it and it closes automatically.
# it also allows to assign file with mode to a variable that can be treated as file variable
import json
from user import User



'''laoding data to the file using json.load()'''
#to save directly to a file we can need to use json libr so we imported json
# with open('Jordan.txt','r') as f:
#     json_data = json.load(f)  # json_data becomes now  a python dictionary
#     user = User.from_json(json_data)
#     print(user.json())








'''wiritng onto a file using json.dump()'''
# writing on to the file
user=User('James')
user.add_movie('Avenger','comic')
user.add_movie('Rush','Crime')
print(user.json())
with open('Jordan.txt','w') as f:
    json.dump(user.json(), f)  # pass a file pointer{while calling change file opening mode}







'''Saving and laoding data in CSV format'''
'''loading from a file'''
# loading from a file
# loading_data_from_file= user.load_from_file('Jordan.txt')
# print(loading_data_from_file.movies)


''' writing to a file'''
# user.add_movie('inception','sic-fi')
# user.add_movie('aquaman','comic')
#
# user.save_to_file()
''' '''

''''"with" contstructor '''
# with open("my_file.txt") as f:
#     f.write("Learning python")
#     print(f.readline())


''' testing appending movies'''
# from movie import Movie
# from user import User
#
# user=User("jordan")
# my_movie=Movie('abc','ncd',True)
# user.movies.append(my_movie)
#
#
#
# print(user.watched_movies())