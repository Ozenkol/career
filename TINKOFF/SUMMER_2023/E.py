n = int(input())
count = 0

my_list = list(map(int, input().split()))
good_lists = []
for position in range(len(my_list)):
    for interval in range(len(my_list) - position):
        sub_list = my_list[position:(position+interval+1)]
        if sum(sub_list) == 0:
            good_lists.append(sub_list)

for position in range(len(my_list)):
    for interval in range(len(my_list) - position):
        sub_list = my_list[position:(position+interval+1)]
        for list_element in good_lists:
            if str(list_element).strip("[]") in str(sub_list).strip("[]"):
                count = count + 1
                break

print(count)