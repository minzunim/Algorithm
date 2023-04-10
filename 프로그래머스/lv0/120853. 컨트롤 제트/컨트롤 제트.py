def solution(s):
    # 스택을 배열로 선언
    stack = []
    # 문자열을 공백 기준으로 나눠서 배열로 만든 다음 반복문
    for a in s.split():
        if a != 'Z':    # 만약 요소가 'Z'가 아니라면 스택에 요소를 추가
            stack.append(int(a))
        else:
            stack.pop() # 만약 요소가 'Z'라면 스택에 있는 마지막 요소를 제거
        
    return sum(stack)   # 스택 안에 있는 요소들의 합계 구하기
