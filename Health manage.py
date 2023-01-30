print("Health management System")

import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if (c == 1):
            value = input("Type here \n")
            with open("Ram-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written: ")
        elif (c == 2):
            value = input("type here \n")
            with open("Ram-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if (c == 1):
            value = input("Type here \n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n:")
            print("successfully written")
        elif (c == 2):
            value = input("Type here \n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if (c == 1):
            value = input("Type here \n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n:")
            print("successfully written")

        elif (c == 2):
            value = input("type here \n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1(Ram),(2(rohan),(3(hammad): ")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            with open("Ram-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Ram-food.txt") as op:
                for i in op:
                    print(i, end="")

    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            with open("Ram-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")


    else:
        print("Please enter the valid input ")


a = int(input("Press 1 for lock the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Ram 2 for rohan and 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for Ram 2 for rohan and 3 for hammad "))
    retrieve(b)































