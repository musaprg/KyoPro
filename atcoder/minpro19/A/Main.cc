#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,K;
    cin>>N>>K;
    if(N/2+N%2>=K) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    return 0;
}
