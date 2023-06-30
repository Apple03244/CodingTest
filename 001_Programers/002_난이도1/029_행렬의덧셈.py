'''import numpy as np
def solution(x,y):
    return list(map(list,list(np.array(x)+np.array(y))))

solution=lambda x,y: list(map(list,list(np.array(x)+np.array(y))))

def soluiton(x,y):
    for i in range(len(x)):
        for j in range(len(x[0]))
'''

def solution(x,y):
    result=[[0 for j in range(len(x[0]))] for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j]=x[i][j]+y[i][j]
    return result

solution([[1,2],[2,3]],[[3,4],[5,6]])