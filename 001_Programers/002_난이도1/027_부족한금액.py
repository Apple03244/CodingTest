def solution(price, money, count):
    return 0 if money-sum([(i+1)*price for i in range(count)])>=0 else sum([(i+1)*price for i in range(count)])-money