checklist = list()

# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    return checklist[index]


# UPDATE
def update(index, item):
    checklist[index] = item


# DELETE
def delete(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(f"{index} {list_item}")
        index += 1


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    delete(1)

    print(read(0))

    list_all_items()


test()
