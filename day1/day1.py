input = open("day1/day1input.txt", "r")

arr1 = []
arr2 = []
total = 0
count = 0

for i in input:
    arr1.append(i[:5])
    arr2.append(i[8:13])

arr1.sort()
arr2.sort()

for idx, i in enumerate(arr1):
    total += abs(int(i) - int(arr2[idx]))
    count += 1
