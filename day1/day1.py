
f = open("input.txt", "r")


# PROBLEM 1

total_list = []
count = 0

for line in f:
    if line != "\n":
        count += int(line)
    else:
        total_list.append(count)
        count = 0

print(f"Highest Calories for problem 1: {max(total_list)}")

# PROBLEM 2

n = 3
sum_n = 0

for i in range(0, 3):
    top = max(total_list)
    sum_n += top
    total_list.remove(top)

print(f"Top N highest calories for problem 2: {sum_n}")
