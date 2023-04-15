def solution(s):
    arr = list(s)
    if len(arr) == 4 or len(arr) == 6:
        if s.isdigit():
            return True
        return False
    return False

# a~z 중에서 하나라도 포함되어 있으면 false
