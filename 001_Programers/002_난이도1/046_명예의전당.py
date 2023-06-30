def solution(k, score):
    rank=[]
    result=[]
    for x in score:
        rank.append(x)
        rank.sort(reverse=True)
        if len(rank)>k:
            rank.pop()
        result.append(rank[-1])
    return result

solution(3,[10,100,20,150,1,100,200])
A=[10,100,20,150,1,100,200]
A.pop()
A