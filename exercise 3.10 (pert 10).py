## sort array with numbers
import random

data = random.sample(range(1, 10), 6)
print('data :', data)

temp = 0
for i in range (len(data)-1, 0, -1):
    for j in range(i):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp

print('data :', data)