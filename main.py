import os
import sys


def start():
    start_input = input(f"{create_password}/{create_username}: ")
    if start_input == "whoami":
        print()
        print(f"Username: {create_username}")
        print(f"Password: {create_password}")
        input()
        start()
    elif start_input == "clear":
        os.system("cls")
        start()
    elif start_input == "color":
        print()
        type_color = input("Color: ")
        if type_color == "4":
            os.system("color 4")
            print()
            start()
        else:
            print()
            print("Error: Wrong user input.")
            input()
            start()
    elif start_input == "exit":
        sys.exit()
    else:
        print()
        print("Error: Wrong user input.")
        input()
        start()


print("Create a new user:")
print()
create_username = input("Username: ")
print()
print("Create a password:")
print()
create_password = input("Password: ")

os.system("cls")
start()
