#include <stdio.h>
#include <stdlib.h>
#include<math.h>

long long func(long long n)
{
    if(n==1 || n==2)
    {
        return 1;
    }       

    if(n%2==0)
    {
        return func(n-1)+(2*func(n-2));
    }
    
    else
    {
        return (func(n-1)*2)+1;
    }
}
int main()
{
    long long x,n,r;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld",&n);
        x=pow(2,n);
        r=func(n);
        printf("%lld %lld ",r,x);
    }
    return 0;
}
