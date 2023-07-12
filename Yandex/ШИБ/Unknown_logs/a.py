import sys
import re

for line_string in iter(sys.stdin.readline, ''):
  line = line_string.rstrip()
with open('events.txt', 'r') as f:
    for line in f.readlines():
        line = line_string.rstrip()
        date = re.search(r'date=[0-9]+\-[0-9]+\-[0-9]+', line)
        date = date.group()
        print(date)