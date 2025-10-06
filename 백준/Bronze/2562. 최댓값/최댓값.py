max_num = 0
count = 0
current = 0
max_count = 0

while True:
    try:
        current = int(input())
        count += 1
        if max_num < current:
            max_num = current
            max_count = count
        
    except EOFError:
        break

print(max_num)
print(max_count)