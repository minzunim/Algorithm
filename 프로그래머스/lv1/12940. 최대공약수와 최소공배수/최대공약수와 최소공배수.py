def solution(n, m):
    sol =[]
    #최대 공약수
    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i ==0:
            sol.append(i)
            break

    #최소 공배수
    for j in range(max(n,m), (n*m)+1):
        if j%n == 0 and j%m  ==0:

            sol.append(j)
            break
    return sol
