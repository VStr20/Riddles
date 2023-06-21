# You are blindfolded, and are told if you can correctly solve the following, the blindfold will be removed. You are given 99 coins that are heads up, and an unknown number of coins that are tails up. You never remove the blindfold, you do not peek, …. You can count the coins, put them in arbitrary many piles, flip whichever coins you want, but remember, when you flip and when you sort, you DO NOT know which ones are heads up, which are tails up. In the end, you must end up with just two piles, each containing an equal number of heads. How do you do this?

import numpy as np
import random
# number of coins n
count = 99
# coin_face = np.zeros()
for i in range(100, 200):
    coin_face = np.zeros(i+1)
#     print(len(coin_face))
    count = 99
    while(count>0):
        k = random.randint(0, i)   # set any 99 coins to be heads
#         print(k)
        if(coin_face[k] == 0):
            coin_face[k] = 1
            count -= 1
        else:
            continue
    for q in range(36):    # choose random 99 samples in pile_1
        pile_1 = np.random.choice(coin_face, size=99, replace=False)
        #  turn coins in pile 1
        heads_pile_1_turned = 0    # after turning
        heads_pile_1_original = 0    # before turning
        for p in range(len(pile_1)):
            if(pile_1[p] == 0):
                heads_pile_1_turned += 1
            else:
                heads_pile_1_original += 1
        heads_pile_2 = 99 - heads_pile_1_original
        if(heads_pile_2 == heads_pile_1_turned):
            print("For i =", i, "Iteration =", q, "Method Worked") 
    
    
    
