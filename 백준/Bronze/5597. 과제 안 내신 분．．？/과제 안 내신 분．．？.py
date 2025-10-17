students = 30 * [0]

for _ in range(28):
    submitted = int(input())
    students[submitted - 1] = 1
    
for i, s in enumerate(students):
    if s != 1:
        print(i + 1)