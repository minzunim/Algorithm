def solution(s):
    answer = ''
    if len(s) % 2 != 0:
        return s[len(s) // 2: len(s) // 2 + 1]
    return s[len(s) // 2 - 1: len(s) // 2 + 1]

# 5 -> 2 [2:3] => 5 // 2 [len(s) // 2: len(s) // 2 + 1]
# 4 -> 1, 2 [1:3]