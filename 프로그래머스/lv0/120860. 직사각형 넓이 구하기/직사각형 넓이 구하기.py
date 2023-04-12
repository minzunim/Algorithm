def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    return (max(x) - min(x)) * (max(y) - min(y))

# max(x) - min(x) X max(y) - min(y)