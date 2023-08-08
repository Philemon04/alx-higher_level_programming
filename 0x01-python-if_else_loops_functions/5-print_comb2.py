#!/usr/bin/python3
for i in range(0, 100):
    if(i < 10):
        print(0, end=f"{i}, ")
    elif(i == 99):
        print(i, end="")
    else:
        print(i, end=", ")
