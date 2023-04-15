def solution(numbers):
    return sum(list(set(list(range(10))) - set(numbers)))
