'''
def solution(numbers):
    result=set([])
    for i in range(len(numbers)):
        if i==len(numbers)-1:
            break
        for j in range(i+1,len(numbers)):
            result.add(numbers[i]+numbers[j])
    return result
우씨...이거 안되네....
'''
def soltuion(numbers):
    result={}
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            break
        for j in range(i + 1, len(numbers)):
            result[numbers[i]+numbers[j]]=1
    answer=list(result.keys())
    answer.sort()
    return answer

soltuion([2,1,3,4,1])
dir(list)