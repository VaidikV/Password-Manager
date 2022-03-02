from random import choice, randint, shuffle
import pyperclip


def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Making 3 lists containing random elements from the specified list mentioned above in the form of list compression.
    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    pass_list = random_letters + random_numbers + random_symbols
    # Randomizing the list and then converting it to a string.
    shuffle(pass_list)
    # Converts the list into a string and puts "" in between every element.
    password = "".join(pass_list)
    pyperclip.copy(password)
    return password
    # password_entry.delete(0, END)
    # password_entry.insert(0, password)
    


print(password_generator())
