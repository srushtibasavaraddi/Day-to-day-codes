#include <iostream>
using namespace std;

int iseven(long long x)
{
    if (x%2==0)
        return 1;
    else
        return 0;
}

int main() {
    long long T,P1,P2,sum=0,K;
	cin >> T ;
	while(T--)
	{
	    cin >> P1 >> P2 >> K;
	    sum=(P1 + P2) / K;
	    if(iseven(sum))
	        cout << "CHEF" << endl;
	    else
	        cout << "COOK" << endl;
	    
	}
	return 0;
}

