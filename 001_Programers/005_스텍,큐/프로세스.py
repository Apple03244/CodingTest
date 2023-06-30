def solution(nlist,n):
    copy_list=nlist.copy()
    copy_list.sort(reverse=True) #결과 기준
    result=[None for x in range(len(nlist))]
    i=0
    j=0
    tem=len(nlist)
    result=1
    while not result[n]:
        if nlist[i%temp]==copy_list[j]:
            result[i%temp]=j
            i+=1
            j+=1
        else:
            i+=1
    return result