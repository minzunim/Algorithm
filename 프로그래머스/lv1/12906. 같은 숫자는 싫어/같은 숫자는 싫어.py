def solution(arr):
    stack = []
    
    for i in range(len(arr)):
        if len(stack) == 0 or stack[-1] != arr[i]:
            stack.append(arr[i])
    return stack
