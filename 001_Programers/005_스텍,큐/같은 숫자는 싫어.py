def solution(array):
    temp=None

    answer=[]
    for x in array:
        if x!=temp:
            answer.append(x)
            temp=x
    return answer

solution([1,1,1,2,2,3,1,3])