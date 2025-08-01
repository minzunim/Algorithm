def solution(answers):
    # 각 사람들의 문제 푸는 패턴 확인
    # 1번: 12345 -> 1~5 순차
    # 2번: 21232425 -> 반복
    # 3번: 3311224455 -> 반복
    first = [1,2,3,4,5]    
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    array = [0, 0, 0]
    length = len(answers)
    
    for i in range(length):
        if answers[i] == first[i % len(first)]:
            array[0] += 1
        
        if answers[i] == second[i % len(second)]:
            array[1] += 1
                
        if answers[i] == third[i % len(third)]:
            array[2] += 1
        
    result = []
    max_count = max(array)
    for i in range(len(array)):
        if max_count == array[i]:
            result.append(i + 1)
    return result