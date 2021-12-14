# Author MB 12/14/2021

from random import randint

def clone_name():
    while True:
        ans = (input("Do you want to name this trooper, Y or N: "))
        if ans == 'Y':
            clonenam = "New clone trooper name: CT-{0}".format(randint(0, 9999))
        print(clonenam)
        if ans == 'N':
            finished = list(clonenam)
            print(finished)
clone_name()