

def wizard(N,owners,duels):
    changes=0
#    print(duels[0])
    #check first character
#    print(duels[0][0])
    for i in range(N):
        if duels[i][1]== owners:
            owners=duels[i][0]
            changes+=1
    print(owners,changes)
    



wizard(3,"A",["BA","CB","DA"])