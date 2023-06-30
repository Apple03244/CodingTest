def solution(d:list,budget:int):
    d.sort(reverse=True)
    result=[]
    while sum(result)<=budget:
        result.append(d.pop())
        if not d:
            break
    if sum(result)>budget:
        result.pop()
    return len(result)
