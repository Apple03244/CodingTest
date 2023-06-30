import numpy as np
def solution(park, routes):
    A=np.array(list(map(list,park)))
    start=list(map(int,np.where(A=="S")))
    size=list(A.shape)

    def rout(x):
        id_x = x.split()
        idx, n = id_x[0], int(id_x[1])
        temp = {"N": ["H", -1, n], 'S': ["H", 1, n], 'E': ["W", 1, n], 'W': ["W", -1, n]}
        return temp[idx]  # 인덱스,방향,횟수




A=np.array(list(map(list,["SOO","OOO","OOO"])))
list(map(int,np.where(A=='S')))
list(A.shape)
bool(list(A[np.where(A=='X')]))
x=[0,1]
any(x)

A[x[0],x[1]]