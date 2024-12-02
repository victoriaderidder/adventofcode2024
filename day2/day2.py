import copy

with open('day2/day2input.txt', 'r') as file:
    lines = [line.strip().split() for line in file]

# part 1 answer = 680
total = 0
unsafe = copy.deepcopy(lines)

for top_idx, line in enumerate(lines):
    report_safe = True
    increasing = False
    decreasing = False
    for idx, i in enumerate(line[:-1]):
        difference = int(i) - int(line[idx+1])
        if difference not in range(1, 4) and \
            difference not in range(-3, 0):
            if report_safe:
                del unsafe[top_idx][idx]
            report_safe = False
        if difference > 0:
            increasing = True
        if difference < 0:
            decreasing = True
    if report_safe == True and increasing != decreasing:
        total += 1
        unsafe[top_idx] = []       

print(total) 

# part 2 answer = 710
for top_idx, line in enumerate(unsafe):
    report_safe = True
    increasing = False
    decreasing = False
    if line != []:
        for idx, i in enumerate(line[:-1]):
            difference = int(i) - int(line[idx+1])
            if difference not in range(1, 4) and \
                difference not in range(-3, 0) or all([increasing, decreasing]):
                report_safe = False
            if difference > 0:
                increasing = True
            if difference < 0:
                decreasing = True
        if report_safe == True:
            total += 1

print(total)