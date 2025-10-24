from collections import Counter

n = int(input())
count = 0

for _ in range(n):
    word = input()
    list = [ word[i] for i in range(len(word)) if i == 0 or word[i] != word[i - 1] ]
    count_dict = Counter(list)
    if max(count_dict.values()) == 1:
        count += 1

print(count)