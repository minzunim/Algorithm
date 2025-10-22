from collections import Counter

word = input().upper()
count_dict = Counter(word)

max_value = max(count_dict.values())
max_keys = [ char for char, count in count_dict.items() if count == max_value ]

print('?' if len(max_keys) > 1 else max_keys[0])
        
