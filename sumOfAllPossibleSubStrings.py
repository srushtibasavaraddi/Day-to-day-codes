# 6, 7, 8, 9, 67, 78, 89, 678, 789, 6789
#        Frequency in substrings at positions
# Digit   Unit    Ten     Hundred     Thousand        Sum
# 6       1       1       1           1           = 6*1*1111
# 7       2       2       2                       = 7*2*111
# 8       3       3                               = 8*3*11
# 9       4                                       = 9*4*1
n=(input())
n=n[::-1]
ans=0
l=len(n)
ones=1
mod=1000000007
for i in n:
    i=int(i)
    # print(ones,l)
    ans= (ans+i*l*ones)%mod
    l=l-1
    ones=(ones*10+1)%mod
print(ans)