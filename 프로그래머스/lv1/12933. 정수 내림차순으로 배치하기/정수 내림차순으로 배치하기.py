def solution(n):
    return int(''.join(map(str, list(map(int, sorted(str(n), reverse=True))))))
