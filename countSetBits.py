def  countSetBits(n): 
    c=0
    while(n): 
        count+=n&1
        n>>=1
    return c 
  
