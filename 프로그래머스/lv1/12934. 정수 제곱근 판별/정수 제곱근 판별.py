import math

def solution(n):
    for num in range(1, n+1):
        if num ** 2 == n:
            return (num + 1)**2
    return -1