def duplicate_list(my_list):
    return [val for val in my_list for _ in (0, 1)]


def add_to_list(my_list, element):
    my_list.append(element)


def remove_from_list(my_list):
    print(my_list[0])
    my_list.pop(0)


n = int(input())
res_list = []


for i in range(n):
    input_command = list(map(int, input().split()))
    if len(input_command) == 2:
        add_to_list(res_list, input_command[1])
        #print(res_list)
    elif len(input_command) == 1 and input_command[0] == 2:
        res_list = duplicate_list(res_list)
        #print(res_list)
    else:
        remove_from_list(res_list)