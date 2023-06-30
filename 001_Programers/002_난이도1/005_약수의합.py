def solution(n):
    a=[m for m in range(1,n+1) if n%m==0]
    return sum(a)

solution(12)