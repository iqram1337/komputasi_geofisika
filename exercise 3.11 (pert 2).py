import numpy as np

## cara leibniz
a = 8
ans = 0

for i in range(100+1):
    x = (1/((4*i)+1)) * (1/((4*i)+3))
    x = x*a
    ans = ans + x

print('Leibniz Scheme :', ans)



## cara Euler
a = 6
ans = 0

for i in range(1, 100+1):
    x = (1/(i**2))
    x = x*6
    ans = ans + x

print('Euler Scheme :', np.sqrt(ans))