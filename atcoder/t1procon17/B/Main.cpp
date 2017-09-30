#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int
#define INF (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll N; cin>>N;
    ll ix=0,v;
    for(ll i = 0; i < N; i++){
        ll a,b;
        cin>>a>>b;
        if(ix<a){
            ix = a;
            v = b;
        }
    }
    cout<<ix+v<<endl;
    return 0;
}