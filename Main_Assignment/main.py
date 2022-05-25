from Main_Assignment.page.login_page import login
from Main_Assignment.page.register_page import register_user
from Main_Assignment.Lists.movieList import MovieList
from Main_Assignment.Lists.userList import UserList

movies = MovieList()
users = UserList()

while True:
    print("******Welcome to BookMyShow*******")
    print("1. Login")
    print("2. Register new account")
    print("3. Exit")

    inp = input()
    if inp == '1':
        login(movies, users)
        for i in movies.mlist.values():
            print(i)
    elif inp == '2':
        register_user(movies, users)
        for i in movies.mlist.values():
            print(i)
        # print(users)
    else: exit(0)

