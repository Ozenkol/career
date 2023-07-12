n = int(input())

for i in range(1, n+1):
    sigma = 4*((i*(i+1)*(2*i+1))/6) - i - 2*(i**2)
    print(int((2*i - 1)**3 - sigma), end=" ")