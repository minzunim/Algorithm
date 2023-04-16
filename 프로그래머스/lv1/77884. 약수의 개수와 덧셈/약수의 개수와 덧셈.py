def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        count = sum(1 for i in range(1, num + 1) if num % i == 0)
        answer += num if count % 2 == 0 else -num
    return answer

