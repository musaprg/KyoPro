#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    long double N;
    ll P;
    cin>>N>>P;
    ll gmax = pow(P, 1/N);
    for(ll g = gmax; g > 0; --g){
        ll gn = pow(g,N);
        if(P%gn==0){
            cout<<g<<endl;
            break;
        }
    }
    return 0;
}
