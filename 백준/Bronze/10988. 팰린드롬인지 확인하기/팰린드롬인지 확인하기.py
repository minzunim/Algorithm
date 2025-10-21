letters = input()
length = len(letters)
is_palindrome = 1

for i in range(length // 2):
    if letters[i] != letters[length - i - 1]:
        is_palindrome = 0
        break
    else:
        continue

print(is_palindrome)
        