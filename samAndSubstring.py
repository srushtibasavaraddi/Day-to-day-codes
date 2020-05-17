from sys import stdin,stdout
n=(input())
n=n[::-1]
ans=0
l=len(n)
ones=1
mod=1000000007
for i in n:
    i=int(i)
    # print(ones,l)
    ans= (ans+(i*l*ones))%mod
    l=l-1
    ones=(ones*10+1)%mod
print(ans)

