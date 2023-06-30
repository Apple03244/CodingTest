def solution(s): #대문자가 소문자보다 작다?
    ls=list(s)
    ls.sort(reverse=True)
    return "".join(ls)