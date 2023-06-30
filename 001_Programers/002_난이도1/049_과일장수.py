def solution(k, m, score):
    score.sort()
    box=[]
    while len(score)>=m:
        fruits=[]
        for i in range(m):
            fruits.append(score.pop())
        box.append(fruits)
    return sum(list(map(lambda x:min(x)*len(x),box)))

solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])