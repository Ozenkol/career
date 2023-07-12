n, m, k = map(int, input().split())
t = 0
if n > m:
    t = (n//m)
    t = t*k
    if n % m != 0:
        t = t + 1

else:
    t = m * k

print(t)



