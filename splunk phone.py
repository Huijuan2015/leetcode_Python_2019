# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

def flipCoin(A): # return number
    if not A:
        return 0
    # first coin is 0
    currCoin = 0
    flipNum_0 = 0
    for coin in A:
        if currCoin != coin:
            flipNum_0 += 1
        currCoin = 1-currCoin
    
    # first coin is 1
    currCoin = 1
    flipNum_1 = 0
    for coin in A:
        if currCoin != coin:
            flipNum_1 += 1
        currCoin = 1-currCoin
    return min(flipNum_0, flipNum_1)
    
    
A = [1,0,1,0,1,1]
num = flipCoin(A)
print (num)

B = [1,1,0,1,1]
num_B = flipCoin(B)
print (num_B)

C = [0,1,0]
num_C = flipCoin(C)
print (num_C)

D = [0,1,1,0]
num_D = flipCoin(D)
print (num_D)