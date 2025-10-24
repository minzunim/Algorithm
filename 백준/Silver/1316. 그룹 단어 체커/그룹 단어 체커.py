from collections import Counter

n = int(input())
count = 0

for _ in range(n):
    word = input()
    prev, cur = '', ''
    list = []

    for char in word:
        cur = char
        if prev != cur:
            list.append(char)
        prev = cur

    count_dict = Counter(list)
    if max(count_dict.values()) == 1:
        count += 1

print(count)