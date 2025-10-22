word = input().upper()
count_dict = {}

for char in word:
    if not count_dict.get(char):
        count_dict[char] = 1
    else:
        count_dict[char] += 1

max_char = max(count_dict, key=count_dict.get)
max_count = 0

for char in count_dict:
    if count_dict[max_char] == count_dict[char]:
        max_count += 1

if max_count > 1:
    print('?')
else:
    print(max_char)
        
