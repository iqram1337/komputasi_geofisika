import numpy as np

## cara leibniz
n = int(input('Masukkan N: '))
print('----------------------------------------------------------')
ans = 0

for i in range(n+1):
    x = (1/((4*i)+1)) * (1/((4*i)+3))
    x = x*8
    ans = ans + x

print('Leibniz Scheme :', ans)



## cara Euler
ans = 0

for i in range(1, n+1):
    x = (1/(i**2))
    x = x*6
    ans = ans + x

print('Euler Scheme :', np.sqrt(ans))
