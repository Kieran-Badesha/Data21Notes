# name = input("Hello what is your name? ")
# age = int(input(f"Nice to meet you {name}. How old are you?"))

# List of films in each category
films_to_watch = {"under_12": ["All Dogs Go to Heaven", "Chicken Little", "The Mighty Ducks", "D2: The Mighty Ducks"],
                  "under_15": ["Forest Gump", "Black Panther", "Home Alone", "Avengers", "Godzilla vs. Kong"],
                  "under_18": ["Nobody", "Zack Snyder's Justice League", "Sound of Metal"],
                  "over_18": ["Fifty Shades Of Grey", "The Wolf Of Wall Street", "Hannibal", "Legend"]
                  }


# ASK for AGE VIA USER INPUT AND GET NAME LIMIT THE AGE
name_prompt = True
age_prompt = True

while name_prompt:
    name = input("Hello what is your name? ").capitalize()
    if name.isalpha():
        name_prompt = False
    else:
        print("Please provide your name in letters")

while age_prompt:
    age = input(f"Nice to meet you {name}. How old are you? ")
    if age.isdigit() and 0 <= int(age) < 130:
        age_prompt = False
    else:
        print("Please provide your answer as a positive whole number")


# FROM THAT GIVE US THE TYPES OF FILM THEY CAN WATCH AT THE CINEMA
if int(age) < 12:
    print(f"In that case these are the films you can watch ")
    print(films_to_watch["under_12"])
elif 12 <= int(age) < 15:
    print(f"In that case these are the films you can watch ")
    print(films_to_watch["under_12"])
    print(films_to_watch["under_15"])
elif 15 <= int(age) < 18:
    print(f"In that case these are the films you can watch ")
    print(films_to_watch["under_12"])
    print(films_to_watch["under_15"])
    print(films_to_watch["under_18"])
else:
    print(f"In that case these are the films you can watch ")
    print(films_to_watch["under_12"])
    print(films_to_watch["under_15"])
    print(films_to_watch["under_18"])
    print(films_to_watch["over_18"])
