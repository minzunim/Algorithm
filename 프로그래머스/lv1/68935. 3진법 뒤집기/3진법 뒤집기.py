def solution(n):
    rev_base = ''
    
    while n > 0:
        n, q = divmod(n, 3)
        rev_base += str(q)
        
    return int(rev_base, 3)