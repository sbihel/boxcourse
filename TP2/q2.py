#! /bin/env/python3
import sys


with open("./outputq1.txt") as f:
    for l in f:
        if int(l.split(" ")[-2]) > int(sys.argv[1]):
            print(l, end="")
