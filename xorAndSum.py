a,b=int(input(),2),int(input(),2)
s=0
for i in range(314159+1):
    s+=a^(b<<i)
print(s%1000000007)