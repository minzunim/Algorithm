def solution(s):
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True