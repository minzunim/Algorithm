def solution(price, money, count):
    total_price = price * (sum(range(1, count + 1)))
    if money > total_price:
        return 0
    return abs(money - total_price)
    
# 1번 money - 100 * 1
# 2번 money - 100 * 1 + 100 * 2
# 3번 money - 100 * 1 + 100 * 2 + 100 * 3
# n번 money - (100 * ( 1 + ... + n ))