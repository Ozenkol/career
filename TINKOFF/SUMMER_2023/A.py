list = list(map(int, input().split()))

sorted_list1 = list
sorted_list2 = list

sorted_list1 = list.copy()
sorted_list2 = list.copy()

sorted_list1.sort()
sorted_list2.sort(reverse=True)

if list == sorted_list2 or list == sorted_list1:
    print("YES")
else:
    print("NO")
