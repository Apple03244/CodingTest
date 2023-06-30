import math

def solution(progresses, speeds):
    days=[math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    answer=[]
    temp=days[0]
    #한번 해보자
    for x in days:
        if x>temp:
            answer.append(days.index(x))
            temp=x
    answer=[0]+answer+[len(days)]
    return [answer[i+1]-answer[i] for i in range(len(answer)-1)]
solution([90,90,90,90],[30,1,1,1])

A=3.14
