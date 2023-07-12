import re

n = int(input())
string = input()

stop = False
for interval in range(4, len(string)+1):
    for position in range(len(string) - interval+1):
        substring = string[position:(interval+position)]
        if 'a' in substring and 'b' in substring and 'c' in substring and 'd' in substring:
            print(len(substring))
            stop = True
            break

    if stop == True:
        break

if stop == False:
    print(-1)
