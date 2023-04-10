def solution(numbers, k):
    answer = 0
    if len(numbers) < 2 * k:
        numbers = numbers * k
        answer = numbers[2 * (k - 1)]
    else:
        answer = numbers[2 * (k - 1)]
    return answer

# 123456123456
# 123123
# 2 -> 2 * 1 (2 * k -1)
# 5 -> 2 * 4 2 * k - 1
# 3 -> 2 * 2