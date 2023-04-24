def solution(arr):
    stack = []
    
    for el in arr:
        if stack[-1:] == [el]:
            continue
        stack.append(el)
    return stack 
