def solution(x,y):
    even,odd=[],[]
    for i in range(x,y+1):
        if len([j for j in range(1,i) if not i%j])%2:
            even.append(i)
        else:
            odd.append(i)
    return sum(even)-sum(odd)

import math as n

solution(13,17)