def solution(s):
    stack = []
    flag = False
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    if len(stack) == 0:
        flag = True
    return flag

print(solution(")"))
        
            