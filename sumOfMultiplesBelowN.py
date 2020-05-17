def sumMul(n,k):
    temp=n//k
    return k*(temp*(temp+1))//2
n,k=map(int,input().split())
print(sumMul(n,k))
