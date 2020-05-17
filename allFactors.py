import math  
  
def printDivisors(n) :   
    # Note that this loop runs till square root 
    i = 1
    while(i <= math.sqrt(n)): 
          
        if (n % i == 0) : 
            if (n / i == i) : 
                print(i)
            else : 
                print( i , n/i) 
        i+=1
  
# Driver method 
print "The divisors of 100 are: "
printDivisors(100) 
