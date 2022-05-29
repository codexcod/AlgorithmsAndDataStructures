array = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5,6,7,8,9,10]
times = 0
for i in range(len(array)):
    for x in range(len(array2)):
        times += 1

print(times)