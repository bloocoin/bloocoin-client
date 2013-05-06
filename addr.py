import os


def addr():
    if os.path.exists("bloostamp"):
        with open("bloostamp") as file:
            return "Your address is: " + file.read().split(":")[0]
    else:
        return "Bloostamp does not exist."
