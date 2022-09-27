from colored import fg
import os
from colorama import Fore


checklist = list()
# ADD COLOR TO OUTPUT
def add_color(item):
    item_color = item.split()

    if item_color[0].upper() == "RED":
        return Fore.RED + item
    elif item_color[0].upper() == "GREEN":
        return Fore.GREEN + item
    elif item_color[0].upper() == "BLUE":
        return Fore.BLUE + item
    elif item_color[0].upper() == "CYAN":
        return Fore.CYAN + item
    elif item_color[0].upper() == "YELLOW":
        return Fore.YELLOW + item
    elif item_color[0].upper() == "WHITE":
        return Fore.WHITE + item
    elif item_color[0].upper() == "BLACK":
        return Fore.BLACK + item
    else:
        return item


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    return add_color(checklist[index])


# UPDATE
def update(index, item):
    checklist[index] = item


# DELETE
def delete(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(Fore.WHITE + f"{index} {add_color(list_item)}")
        index += 1


def mark_completed(index):
    update(index, f"√ {checklist[index]}")


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def select_Fn(fn_code):
    # Create item
    if fn_code.upper() == "C":
        input_item = user_input("Input item: ")
        create(input_item)
    # Read item
    elif fn_code.upper() == "R":
        item_index = int(user_input("Index Number? "))
        while item_index >= len(checklist):
            item_index = int(user_input("Invalid index, please try again: "))
        print(read(int(item_index)))
    # Update item
    elif fn_code.upper() == "U":
        item_index = int(user_input("Index Number? "))
        while item_index >= len(checklist):
            item_index = int(user_input("Invalid index, please try again: "))
        updatedItem = user_input(f"Update {checklist[item_index]} into? ")
        print(Fore.GREEN + f"Successfully changed {checklist[item_index]} into {updatedItem}!")
        update(item_index, updatedItem)
    # Delete item
    elif fn_code.upper() == "D":
        item_index = int(user_input("Index of item to delete? "))
        item = checklist[item_index]
        delete(item_index)
        print(Fore.RED + f"Successfully deleted {item}.")

    # Print all items
    elif fn_code.upper() == "P":
        list_all_items()
    elif fn_code.upper() == "Q":
        return False
    else:
        print(Fore.RED + "Unknown Option")

    return True


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    delete(1)

    print(read(0))

    mark_completed(0)

    list_all_items()

    select_Fn("C")
    select_Fn("R")
    # selectFn("P")
    # selectFn("")
    os.system("clear")


running = True
while running:
    prompt = """\nPlease type an option and press enter: 
C - to add to a list            R - to read from list
U - to update an item           D - to delete an item
P - to show list                Q - Quit
> """
    selection = user_input(Fore.WHITE + prompt)
    os.system("clear")
    running = select_Fn(selection)
