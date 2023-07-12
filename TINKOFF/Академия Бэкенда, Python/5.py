from collections import Counter
n = int(input())
my_list = []
strings = []
ME = 2

for i in range(n):
    my_str = input()
    strings.append(my_str)
    letters = Counter(my_str)
    P_a = letters["a"]/len(my_str)
    P_b = letters["b"]/len(my_str)
    P_c = letters["c"]/len(my_str)
    P_max = max(P_a, P_b, P_c)
    my_list.append(abs(0.3333333 - P_max))

print(my_list)
