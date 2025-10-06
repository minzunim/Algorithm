total = int(input())
numbers = list(map(int, input().split()))
v = int(input())

count_map = {}

for num in numbers:
    if not count_map or not count_map.get(num):
        count_map[num] = 1
    else:
        count_map[num] += 1

print(count_map.get(v, 0))
