def solution(arr):
    # 앞의 숫자와 같은지 확인
    prev = arr[0]
    queue = [prev]
    
    for num in arr[1:]:
        if prev != num:
            queue.append(num)
        prev = num
    return queue