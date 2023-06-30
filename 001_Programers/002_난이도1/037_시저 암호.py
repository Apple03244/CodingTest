def solution(s,n):
    def num(x):
        if x in range(97,123):
            return (x+n-97)%26+97
        elif x in range(65,91):
            return (x+n-65)%26+65
        elif x==32:
            return 32
    ls=list(map(ord,list(s)))
    return ''.join(list(map(chr,list(map(num,ls)))))




ord("a"),ord("z") #26개
ord("A"),ord("Z")

solution("aZ",1)