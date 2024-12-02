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

# part 1 answer = 2066446
for idx, i in enumerate(arr1):
    total += abs(int(i) - int(arr2[idx]))
    count += 1

# part 2 answer = 24931009
arr1_set = set(arr1)
similarity_score = 0
for i in arr1_set:
    for j in arr2:
        if j == i:
            similarity_score += int(i)

print(similarity_score)