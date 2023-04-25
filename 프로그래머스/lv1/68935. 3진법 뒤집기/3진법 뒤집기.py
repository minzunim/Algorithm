def solution(n):
    rev_base = ''
    
    while n > 0:
        n, q = divmod(n, 3)
        rev_base += str(q)
        
    return int(rev_base, 3)

# 몫과 나머지를 함께 출력해주는 divmod() 사용
# 몫이 0이 되기 전까지 나누고 나머지를 문자열로 붙이기
# 주의사항: 나머지가 1의 자리부터 계산되므로 숫자가 거꾸로 출력
