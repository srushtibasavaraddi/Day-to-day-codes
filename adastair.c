#include <stdio.h>
#include <stdlib.h>

int main()
{
   int T;
	int N,K,temp,res;
	int arr[128];
	scanf("%d",&T);
	while(T--)
	{
	    scanf("%d%d",&N,&K);
	    for(int i=0; i<N ; i++)
	    {
	        scanf("%d",&arr[i]);
	    }
	    
	    if((arr[0] % K) != 0)
	    {
	            res=arr[0]/K;
	    }
	     
	   else
	   {
	        res=(arr[0]/K)-1;
	   }

	   for(int i=0;i<N-1;i++)
	    {
	        temp=arr[i+1]-arr[i];
	        if((temp%K)!=0)
	        {
	            res+=temp/K;
	        }
	            
	       else
	       {
	        res+=(temp/K)-1;   
	       }
	           
	    }
	    
	    printf("%d\n",res);
	}
	return 0;
}
