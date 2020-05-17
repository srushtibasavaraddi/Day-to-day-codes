arr=[2,4,2,1,4,6,2,5435,23,33,4,32]
n=len(arr)
def update(bit,i,v):
    i+=1
    while(i<=n):
        bit[i]+=v
        i+=i&(-i)

def construct():
    bit=[0 for i in range(n+1)]
    for i in range(n):
        update(bit,i,arr[i])
    
    return bit

def query(i):
    i+=1
    s=0
    while(i>0):
        s+=bit[i]
        i=i&(i-1)
    return s

bit=construct()
print(bit)
print(query(6))