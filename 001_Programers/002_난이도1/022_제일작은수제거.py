def solution(x):
    n=min(x)
    return [-1] if len(x)==1 else [i for i in x if i!=n]