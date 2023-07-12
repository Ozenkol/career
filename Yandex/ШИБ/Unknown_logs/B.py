import re
import sys


with open("events_need.txt","r") as f:
    for line in f.readlines():
        if re.search(r'"success":false', line):
            print(line)

