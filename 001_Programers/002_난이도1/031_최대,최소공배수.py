import math as mt
def solution(n, m):
    return [mt.gcd(n,m),n*m//mt.gcd(n,m)]

solution(3,12)