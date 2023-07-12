def find_reachable_rooms(n, m, a, k, x, y):
    for i in range(n):
        for j in range(m):
            pass

n, m, q = map(int, input().split())

a = [[0]*n for _ in range(m-1)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]

print(a)

for i in range(q):
    x, y, k = map(int, input().split())
    print(find_reachable_rooms(n, m, a, k, x-1, y-1))

