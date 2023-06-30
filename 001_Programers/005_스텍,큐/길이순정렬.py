def sortlen(numlist):
    nd={x:[] for x in dict.fromkeys(list(map(len,numlist)))}
    for x in numlist:
        nd[len(x)].append(x)

    k=list(nd.keys())
    k.sort()
    result=[]
    for x in k:
        result+=nd[x]
    return result

sortlen(['123','312','12','21'])