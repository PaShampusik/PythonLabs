import os
import re
from time import sleep
from sys import exit
from sys import path


class Task_2:

    current_user = None

    def __init__(self) -> None:
        Task_2.log_in(self)

    def menu(self):
        """Displays basic functions we can do

        1)add element 2)remove element 3) find element 4)list elements
        5)grep(checks a value in container by regex) 6)save 7)log in/sign up 8)load
        9)end program"""

        answer = input(
            "\nChoose a function: \n1) Add element\n2) Remove element\n3) Find element\n4) List elements\n5) Grep(lists elements by regex pattern)\n6) Save\n7) Log in/Sign up\n8) Load collection\n9) End the program\n :::::::> "
        )
        match answer:
            case "1":
                self.current_user.add_element(input("Enter element, you want to add: "))
            case "2":
                self.current_user.remove_element(
                    input("Enter element, you want to remove: ")
                )
            case "3":
                self.current_user.find_element(
                    input("Enter element, you want to find: ")
                )
            case "4":
                self.current_user.list_collection()
            case "5":
                self.current_user.grep(
                    input("Enter pattern, elements by wich do you want to find: ")
                )
            case "6":
                self.current_user.save()
            case "7":
                answer = input("Wanna save your collection?(y/n): ")
                if answer == "y":
                    self.current_user.save()
                    self.log_in()
                else:
                    self.log_in()
            case "8":
                self.current_user.load()
            case "9":
                answer = input("Wanna save your collection?(y/n): ")
                if answer == "y":
                    self.current_user.save()
                    exit(0)
                else:
                    print("Program ended!")
                    exit(0)
            case _:
                print("Wrong input, try again!")
        sleep(1)
        self.menu()

    def log_in(self):
        """Log in or create a new user."""

        #try:
        self.current_user = User(
            input(
                "Here a program for storing a collection of unique elements for different users,\nNow enter a name of user you want to log in or sign up: "
            )
        )
        print("Log in/sign up is successful!")

        if os.path.exists(os.path.join(path[0], "users", f"{self.current_user.name}.txt")):
            answer = input("Do you want to load your  collection?(y/n): ")
            if answer == "y":
                self.current_user.load()
                Task_2.menu(self)
            else:
                Task_2.menu(self)
        else:
            Task_2.menu(self)
        #except:
            #print("Something went wrong!")


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.items = set()

    def load(self) -> None:
        """Loads items for current user from file"""

        try:
            if os.path.exists(os.path.join(path[0], "users", f"{self.name}.txt")):
                f = open(
                    os.path.join(path[0], "users", f"{self.name}.txt"), "r", encoding="utf-8"
                )
                for i in f.read().split():
                    self.items.add(i)
                f.close()
                print("Your coolection is loaded succesfully!")
            else:
                f = open(os.path.join(path[0], "users", f"{self.name}.txt"), "w")
                f.close()
                print("You had no collection, but we created empty one!")
        except:
            print("Something went wrong, try again!")

    def add_element(self, elem: str) -> None:
        """Adding element to collection of unique elements"""

        try:
            self.items |= set(elem.split())
            print("Your element is added successfully!")
        except:
            print("Something went wrong during adding element")

    def remove_element(self, elem) -> None:
        """Removing element to collection of unique elements"""

        try:
            self.items.remove(elem)
            print("Given element removed successfully!")
        except:
            print("Something went wrong during removing element, try again!")

    def find_element(self, elem) -> bool:
        """Finding element in collection of unique elements"""

        try:
            if elem in self.items:
                print("Given element exists in your collection!")

                return True
            else:
                print("No such element in yuor collection!")

                return False
        except:
            print("Something went wrong!")

    def list_collection(self) -> None:
        """Listing elements of collection of unique elements"""
        try:
            print("Here all the elements in your collection.")
            for i in self.items:
                print(i, end=" ")
        except:
            print("SOmething went wrong!")

    def grep(self, pattern) -> None:
        """Finding element in collection of unique elements by regex pattern"""

        pat = f"{pattern}"
        match = re.findall(pat, " ".join(self.items))
        print("Here are all the matches by pattern in your collection: ")

        for i in match:
            print(i, end=" ")

        return None

    def save(self) -> None:
        """Saving collection of unique elements in a file"""

        try:
            if os.path.exists(os.path.join(path[0], "users", f"{self.name}.txt")):
                pass
            else:
                f = open(os.path.join(path[0], "users", f"{self.name}.txt"), "w")
                f.close()
            f = open(
                os.path.join(path[0], "users", f"{self.name}.txt"), "r", encoding="utf-8"
            )
            file = set(f.read().split())
            f.close()
            if file.issubset(self.items):
                f = open(
                    os.path.join(path[0], "users", f"{self.name}.txt"), "w", encoding="utf-8"
                )
                f.truncate()
                for i in self.items:
                    f.write(str(i) + " ")
                f.close()
                print("Save is successful!")

                return None
            answer = input(
                "File content is not a subset of your current collection, are you sure to save it?(y/n)   "
            )
            if answer == "y":
                f = open(
                    os.path.join(path[0], "users", f"{self.name}.txt"), "w", encoding="utf-8"
                )
                f.truncate()
                for i in self.items:
                    f.write(str(i) + " ")
                f.close()
                print("Save is successful!")

                return None
            else:
                print("Save stopped!")

                return None
        except:
            print("Save went wrong!")

            return None
