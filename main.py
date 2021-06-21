

"\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movie_list = []


def menu():
    user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: ")

    while user_input != "q":

        if user_input == "a":
            add_movies()
        elif user_input == "l":
            show_movies(movie_list)
        elif user_input == "f":
            find_movies()
        else:
            print("Unknown command - please try again .")
        
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: ")



def add_movies():
   print("you are here to add movies \n")
   name = input("enter the movie name: ")
   director = input("enter the name of director: ")
   year = int(input("release date: "))

   movie_list.append(
       {
           'name':name,
           'director':director,
           'year':year,
       }
   )

def show_movies(movies):
    for movie in movies:
        show_movie_details(movie)

    
def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")
    

def find_movies():
    # input_find = input("enter name, director or year to search: ")

    # for values in movie_list:
    #     if input_find == values["name"]:
    #         print("found your movies")
    #     elif input_find == values["director"]:
    #         print(f"found your movies the name is {values['name']}")
    #     elif int(input_find) == values['year']:
    #         print("we found the year")
    #     else:
    #         print("search again")

    find_by = input("what property of movie you are looking for? ")
    looking_for = input("what are you searching for? ")

    found_movies = find_by_attribute(movie_list, looking_for, lambda x: x [find_by])

    show_movies(found_movies)


def find_by_attribute(items,expected, finder):
    found = []

    for _ in items:
        if finder(_) == expected:
            found.append(_)

    return found




    
menu()