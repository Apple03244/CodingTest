def solution(close):
    comb=dict.fromkeys([close[x][1] for x in range(len(close))])
    for x in comb.keys():
        comb[x]=[y[0] for y in close if y[1]==x]
    answer=1
    for x in comb.keys():
        answer*=len(comb[x])+1
    return answer-1



test=solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
test
test['eyewear']