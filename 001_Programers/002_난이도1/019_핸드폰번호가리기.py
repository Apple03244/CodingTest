def solution(pn):
    return "".join(["*" for i in range(len(pn[:-4]))])+pn[-4:]
solution("01033334444")