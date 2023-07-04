import random

responce = input("Enter 'y' to roll the dice or 'n' to exit: ")

while responce == 'y':
    no = random.randint(1,6)
    if no == 1:
        print(
            "[-----] \n" +
            "[-----] \n" +
            "[--0--] \n" +
            "[-----] \n" +
            "[-----]"
        )
    if no == 2:
        print(
            "[-----] \n" +
            "[-----] \n" +
            "[-0-0-] \n" +
            "[-----] \n" +
            "[-----]"
        )
    if no == 3:
        print(
            "[-----] \n" +
            "[-----] \n" +
            "[0-0-0] \n" +
            "[-----] \n" +
            "[-----]"
        )
    if no == 4:
        print(
            "[-----] \n" +
            "[-0-0-] \n" +
            "[-----] \n" +
            "[-0-0-] \n" +
            "[-----]"
        )
    if no == 5:
        print(
            "[-0-0-] \n" +
            "[-----] \n" +
            "[--0--] \n" +
            "[-----] \n" +
            "[-0-0-]"
        )
    if no == 6:
        print(
            "[-0-0-] \n" +
            "[-----] \n" +
            "[-0-0-] \n" +
            "[-----] \n" +
            "[-0-0-]"
        )
    responce = 'n'
    responce = input("Enter 'y' to roll the dice or 'n' to exit: ")
