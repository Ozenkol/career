n, s = map(int, input().split())

student_list = []
right_max = []
left_min = []
count = 0

for i in range(n):
    right_left = list(map(int, input().split()))
    right_max.append(right_left[1])
    left_min.append(right_left[0])
    student_list.append(right_left)
    s = s - right_left[0]

student_list.sort()

while s > 0:
    test = s
    for operation in range(s//len(student_list)):
        position = len(student_list) - 1
        while position > 0 and student_list[position][0] < student_list[position][1]:
            print(student_list)
            student_list[position][0] = student_list[position][0] + 1
            position = position - 1
            s = s - 1
        if test == s:
            break
    if test == s:
        break

while s > 0:
    if s % len(student_list) != 0:
        position = s % len(student_list) - 1
        while position > 0 and student_list[position][0] < student_list[position][1]:
            student_list[position] = student_list[position][0] + 1
            position = position - 1
            s = s - 1
        if test == s:
            break
    if test == s:
        break


student_list.sort()
#print(student_list)
print(student_list[len(student_list)//2][0])
