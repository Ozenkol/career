from collections import Counter


def cond_one(my_list):
    for element in my_list:
        if element != 1:
            return False
    return True


def cond(my_list):
    if cond_one(my_list) == True:
            return True
    if len(set(my_list)) == 2:
        diff = my_list[0]

        for i in range(len(my_list)):
            my_list[i] = my_list[i] - diff

        new_list = list(filter(lambda x: x != 0, my_list))
        if len(new_list) == 1:
            for element in new_list:
                if element != 1 and element != -1:
                    return False
            return True
    else:
        return False


n = int(input())

array = list(map(int, input().split()))

stop = False
interval = n
while interval > 0:
    for position in range(0, n - interval+1):
        subarray = array[position:(position+interval)].copy()
        currlist = Counter(subarray).values()
        #print(subarray)
        if cond(list(currlist)) == True:
            print(len(subarray))
            stop = True
            break
    if stop == True:
        break
    interval = interval - 1


