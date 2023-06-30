import numpy as np
def solution(park, routes):
    P=np.array(list(map(list,park)))
    start=[0,0]
    temp=[len(park)-1,len(park[0])-1] #기준
    #초기값 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if P[i,j]=="S":
                start=[i,j]
    #routes 정리
    def rout(x):
        id_x = x.split()
        idx, n = id_x[0], int(id_x[1])
        temp={"N":[0,-1],"S":[0,1],"E":[1,1],'W':[1,-1]} #인덱싱,더할 값
        return temp[idx]+[n] #인덱스,더할 값, 횟수

    #범위 확인
    for y in routes:
        if rout(y)[0]==0:
            for n in range(1,rout(y)[2]+1):
                if start[0] + rout(y)[1] * rout(y)[2] < 0 or start[0] + rout(y)[1] * rout(y)[2] > temp[0]:
                    break
                if P[start[0]+n*rout(y)[1],start[1]]=='X':
                    break
                start[0]+=rout(y)[1]*rout(y)[2]
        else:
            for n in range(1,rout(y)[2]+1):
                if start[1] + rout(y)[1] * rout(y)[2] < 0 or start[1] + rout(y)[1] * rout(y)[2] > temp[1]:
                    break
                if P[start[0],start[1]+n*rout(y)[1]]:
                    break
                start[1]+=rout(y)[1]*rout(y)[2]
    return start

    # if start[rout(y)[0]]+rout(y)[1]*rout(y)[2]<0 or start[rout(y)[0]]+rout(y)[1]*rout(y)[2]>temp[rout(y)[0]]:
    #     pass

    return start


A=np.array(list(map(list,["OSO",'OOO','OOO'])))
A[0,0]
A
A[0:2,0]

solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"])

test=0
for i in range(10):
    if i==5:
        break
    test+=i
test