#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll N,H,W;
    cin>>N>>H>>W;
    int c = 0;
    for(int i = 0; i < N; i++){
        ll a,b;
        cin>>a>>b;
        if(a>=H&&b>=W) c++;
    }
    cout<<c<<endl;
    return 0;
}
