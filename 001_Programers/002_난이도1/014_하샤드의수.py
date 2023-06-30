def solution(x):
    m=sum(map(int,list(str(x))))
    return True if x%m==0 else False