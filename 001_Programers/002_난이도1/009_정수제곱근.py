import math as mt
def solution(n):
    return pow(mt.sqrt(n)+1,2) if mt.sqrt(n)==mt.isqrt(n) else -1

mt.isqrt(12)

solution(16)