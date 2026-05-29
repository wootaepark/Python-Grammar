arr = []

for i in range(0, 20, 2):
    arr.append(i * i)
print(arr)

# 아래와 같이 만들 수도 있음 (python 제공)
array = [i * i for i in range(0, 20, 2)]

print(array)
