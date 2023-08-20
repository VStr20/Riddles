# You have 2N coins of varying denominations (each is a non-negative real number) in a line. 
# Players A and B take turns to choose one coin from either end. 
# Prove A always has a strategy that ensures he ends up with at least as much as B?

import random

def selection(coins, coin_array, suma, sumb, turn):
    sum_coin_array1 = 0
    sum_coin_array2 = 0
    pop = 0
    erase = 0

    for a in range(coins):
        if a % 2 == 0:
            sum_coin_array1 += coin_array[a]
        else:
            sum_coin_array2 += coin_array[a]

    # print(sum_coin_array1, sum_coin_array2)

    if sum_coin_array1 > sum_coin_array2:
        if turn % 2 != 0:
            suma += coin_array[0]
            coin_array.pop(0)
        else:
            if coin_array[0] < coin_array[-1]:
                pop = 1
            else:
                erase = 1
            sumb += max(coin_array[0], coin_array[-1])
            if pop == 1:
                coin_array.pop()
            elif erase == 1:
                coin_array.pop(0)
        coins -= 1
        turn += 1
    elif sum_coin_array1 == sum_coin_array2:
        if turn % 2 != 0:
            if coin_array[0] < coin_array[-1]:
                pop = 1
            else:
                erase = 1
            suma += max(coin_array[0], coin_array[-1])
            if pop == 1:
                coin_array.pop()
            elif erase == 1:
                coin_array.pop(0)
        else:
            if coin_array[0] < coin_array[-1]:
                pop = 1
            else:
                erase = 1
            sumb += max(coin_array[0], coin_array[-1])
            if pop == 1:
                coin_array.pop()
            elif erase == 1:
                coin_array.pop(0)
        coins -= 1
        turn += 1
    else:
        if turn % 2 != 0:
            suma += coin_array[-1]
            coin_array.pop()
        else:
            if coin_array[0] < coin_array[-1]:
                pop = 1
            else:
                erase = 1
            sumb += max(coin_array[0], coin_array[-1])
            if pop == 1:
                coin_array.pop()
            elif erase == 1:
                coin_array.pop(0)
        coins -= 1
        turn += 1

    # print("suma =", suma, "sumb =", sumb)
    # print("coin_array -", end=" ")
    # for coin in coin_array:
    #     print(coin, end=" ")
    # print()

    if coins <= 0:
        return suma, sumb
    else:
        return selection(coins, coin_array, suma, sumb, turn)

def main():
    random.seed()

    suma = 0
    sumb = 0
    turn = 1

    for coins in range(2, 100, 2):
        coin_array = [random.randint(0, 12) for _ in range(coins)]
        print("coin_array -", end=" ")
        for coin in coin_array:
            print(coin, end=" ")
        print()
    
        suma, sumb = selection(coins, coin_array, suma, sumb, turn)
        if(suma>=sumb):
            print("coins =", coins, " and A wins \n")
        else:
            print("B wins \n")

if __name__ == "__main__":
    main()

# Let’s assume that Player A goes first. First, alternately color the coins red and blue.

# Notice that Player A can get all of the red coins by force. 
# Player A’s strategy is to simply pick the coin at whichever end of the sequence that is red. 
# After doing so, the board will have two blue coins at both ends. 
# No matter what Player B’s pick is, after his turn Player B will reveal a red coin at some end. 
# Player A will then pick that red coin. This goes on until all coins are gone.

# Player A can also get all of the blue coins by force, by the same logic. 
# This means that Player A has a choice — he can get all the blue coins 
# (and let Player B get all the red coins) or get all the red coins 
# (and let Player B get all the blue coins). 
# Since one option will always be equal or better than the other option, Player A can never lose this game.

# Notice that this only works since we had an even number of coins to start off with. 
# If we had an odd number of coins, both ends of the sequence are colored the same, 
# and Player A isn’t able to arbitrarily choose between getting all the red coins vs. getting all the blue coins.

# Also notice that we didn’t need the constraint that all coin values are non-negative, since this strategy works regardless!
