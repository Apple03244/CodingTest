def solution(array, commands):
    result=[]
    temp=[]
    for x in commands:
        temp=array[x[0]-1:x[1]]
        temp.sort()
        result.append(temp[x[2]-1])
    return result
solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])