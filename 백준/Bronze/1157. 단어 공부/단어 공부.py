from collections import Counter

word_dict = Counter(input().upper())
max_count = max(word_dict.values())
max_chars = [ char for char, count in word_dict.items() if count == max_count ]
print('?' if len(max_chars) > 1 else max_chars[0])


        
