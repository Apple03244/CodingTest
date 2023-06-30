def solution(nlist):
    nlist.sort()
    answer=True
    for x in range(len(nlist)):
        if nlist[x]==nlist[x+1][:len(nlist[x])]:
            answer=False
            break
    return answer