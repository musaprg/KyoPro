#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    int K = N/2;
    if(N%2!=0){
        cout<<K+1<<endl;
        cout<<1<<endl;
    }else{
        cout<<K<<endl;
    }
    for(int i=0;i<K;i++)
        cout<<2<<endl;
    return 0;
}
