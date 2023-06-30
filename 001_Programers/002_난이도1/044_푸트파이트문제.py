def solution(food):
    result=[]
    cutls=list(map(lambda x:x//2,food))
    for i in range(len(cutls)):
        if i==0:
            pass
        for j in range(cutls[i]):
            result.append(i)
    return "".join(list(map(str,result+[0]+result[::-1])))


    #1==0
    return cutls
solution([1, 3, 4, 6])

