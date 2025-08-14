def solution(arr):
    # arr = [0, -9]
    # 연속적으로 나타나는 숫자는 모두 제거
    # 순서 유지
    queue = []
    prev = None
    
    for num in arr:
        cur = num
        if prev != cur:
            queue.append(cur)
            prev = cur
    return queue