def solution(players, callings):
    for x in callings:
        players.remove(x)
        players.insert(0,x)
    return players


solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])