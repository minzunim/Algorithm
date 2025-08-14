import math

def solution(progresses, speeds):
    # 진도가 100일 때 서비스 반영
    # 앞에 있는 기능이 배포될 때 함께 배포
    # 큐...?
    # 각 기능이 며칠 작업 후 배포가 가능한지 큐에 저장
    queue = []
    
    for p, s in zip(progresses, speeds):
        days = math.ceil((100 - p) / s) # 추가 작업 시간
        queue.append(days)
    
    prev = queue[0]
    count = 1
    result = []
    
    for q in queue[1:]:
        if prev >= q:
            count += 1
        else:
            result.append(count)
            count = 1
            prev = q
    result.append(count)
    return result
    
    
        