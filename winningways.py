import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def xorArray(arr, n): 
  
    res = 0
    for i in range(0, n): 
        res = res ^ arr[i] 
  
    return res 
  
# Function to return the count of ways 
# to play the first move optimally 
def getTotalWays(arr, n): 
  
    # XOR of all the array elements 
    xorArr = xorArray(arr, n) 
  
    # The player making the first move 
    # can't win the game no matter 
    # how optimally he plays 
    if xorArr == 0: 
        return -1
  
    # Initialised with zero 
    numberOfWays = 0
  
    for i in range(0, n):  
  
        # requiredCoins is the number of coins the 
        # player making the move must leave in the 
        # current pile in order to play optimally 
        requiredCoins = xorArr ^ arr[i] 
  
        # If requiredCoins is less than the current 
        # amount of coins in the current pile 
        # then only the player can make an optimal move 
        if requiredCoins < arr[i]: 
            print(requiredCoins,arr[i])

            numberOfWays += ncr(arr[i],requiredCoins)
  
    return numberOfWays 
  
# Driver code 
if __name__ == "__main__": 
    # Coins in each pile 
    arr = [1,1] 
    n = len(arr)   
    print(getTotalWays(arr, n)) 