def solution(n):
    return min([m for m in range(1,n) if n%m==1])