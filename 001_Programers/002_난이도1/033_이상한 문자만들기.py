def solution(s=str):
    def change(x=list):
        return x[1].lower() if x[0]%2 else x[1].upper()

    idx=0
    idx_l=[]
    for i in s:
        if i!=" ":
           idx_l.append(idx)
           idx+=1
        else:
            idx=-1
            idx_l.append(idx)
            idx+=1

    return "".join(list(map(change,zip(idx_l,list(s)))))

solution("try hello world")
len("try hello world")

if " ":
    print("참?")