def solution(arr, divisor):
    result=[]
    for x in arr:
        if not x%divisor:
            result.append(x)
    result.sort()
    if not result:
        result=[-1]
    return result
solution([5, 9, 7, 10],5)