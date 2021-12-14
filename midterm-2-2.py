# Author MB 12/14/2021

invelo = input("What is the intial velocity: ")
finvelo = input("What is the final velocity: ")
t = input("What is the time in seconds: ")
result = ((int(invelo) / int(t)) + (int(finvelo) / int(t))) / 2
print("The average acceleration is {0}m/s, with intial velocity at {1}m/s, and time at {2}s, and final velocity at {3}m/s".format(result, invelo, t, finvelo))


