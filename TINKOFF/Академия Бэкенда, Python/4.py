q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    sigma = 1
    for j in range(l, r+1):
        s = 1
        #print(sigma)
        if j % 9 == 0:
            s *= 9
        else:
            s *= (j % 9)
        sigma *= s
    if sigma % 9 == 0:
        res = 9
    else:
        res = sigma % 9
    #print(sigma)
    print(res)