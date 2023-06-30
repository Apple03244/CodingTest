def solution(answers):
    rule=dict(zip([1,2,3],[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]))
    rank=dict.fromkeys([1,2,3],0)
    for person in rank:
        for i in range(len(answers)):
            if rule[person][i%len(rule[person])]==answers[i]:
                rank[person]+=1
    return [x for x in rank if rank[x]==max(list(rank.values()))]


solution([1,2,3,4,5])