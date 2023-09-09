
WIN = 1
LOSS = 0
DRAW = .5
initial_rating  = 1200
D = 400
K = 32

def elo1v1(pa,pb,outcome):
    Ea = 1/(1+10**((pb.value-pa.value)/D))
    rating_change = int(K*(outcome-Ea))
    pa.value = pa.value+rating_change
    pb.value = pb.value-rating_change
    return {
            'Player a': pa.name,
            'Player b':pb.name,
            'pa value':pa.value,
            'pb value':pb.value,
            'Expected a':Ea,
            'Expected b':1-Ea,
            'outcome':outcome,
            'rating change':rating_change,
            'rating a':pa.value,
            'rating b':pb.value}

def elo5v5(ta,tb,outcome):
    EaArray  = []
    # calc all Ea
    for playa in ta.players:
        rescom = []
        for playb in tb.players:
            ressing = elo1v1(playa,playb,outcome)
            rescom.append(ressing['Expected a'])
        EaArray.append(rescom)
    SummationEa = []
    for r in EaArray:
        SummationEa.append(sum(r)/5)
    #Transpose matrix
    EaArray = [[EaArray[j][i] for j in range(len(EaArray))] for i in range(len(EaArray[0]))]
    #Summation Ea
    for r in EaArray:
        SummationEa.append((5-sum(r))/5)
    rating_changes = []
    for Ea in SummationEa[:5]:
        rating_change = int(K*(outcome-Ea))
        rating_changes.append(rating_change)
    for Ea in SummationEa[5:10]:
        rating_change = int(K*(1-outcome-Ea))
        rating_changes.append(rating_change)

    return rating_changes


def print_res(ta,ratings):
    i = 0
    print("=== Team ",ta.name," ====")
    for p in ta.players:
        print("Player: ",p.username," Rating: ",p.value," Rating Change: ",ratings[i])
        i= i+1
    


if __name__== '__main__':
    from util.teamgen import generateteam
    from random import randint
    ta,tb = generateteam(2)
    outcome = randint(0,1)
    res = elo5v5(ta,tb,outcome)
    if outcome:
        print("TEAM 0 WON")
    else:
        print("TEAM 1 WON")
    print_res(ta,res[:5])
    print_res(tb,res[5:10])
