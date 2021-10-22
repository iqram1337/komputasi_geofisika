### COMPUTE PI
import numpy as np
import matplotlib.pyplot as plt

n = int(input('Masukkan N: '))
print('----------------------------------------------------------')

## cara leibniz
leibniz_error = []
for i in range(n):
    leibniz_error.append(0)
ans1 = 0

for i in range(n-1):
    ans1 = ans1 + (1/((4*i)+1)) * (1/((4*i)+3))
    leibniz_error[i+1] = np.pi - 8*ans1
ans1 = 8*ans1

print('Metode Leibniz :', ans1)
print('Leibniz error  :', np.abs(np.pi-ans1))
print('')


## cara Euler
euler_error = []
for i in range(n):
    euler_error.append(0)
ans2 = 0

for i in range(1, n):
    ans2 = ans2+(1/(i**2))
    euler_error[i] = np.pi - np.sqrt(6*ans2)
ans2 = np.sqrt(6*ans2)

print('Metode Euler :', ans2)
print('Euler error  :', np.abs(np.pi-ans2))


## ploting grafik error Leibniz dan Euler
sumbu_x = [i for i in range(n)]

plt.plot(sumbu_x, leibniz_error, 'b-', label = 'Leibniz')
plt.plot(sumbu_x, euler_error, 'r--', label = 'Euler')

plt.xlabel('N')
plt.ylabel('Leibniz & Euler Error')

plt.legend()


plt.show()
