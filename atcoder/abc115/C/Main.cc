#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,K;
    cin>>N>>K;
    vector<ll> hh;
    vector<ll> dhh;
    for(int i = 0; i < N; i++){
        ll tmp;
        cin>>tmp;
        hh.emplace_back(tmp);
    }
    sort(hh.begin(), hh.end());

    int ans = INFTY;
    for(int i = 0; i < N-K+1; i++){
        ll tmp = hh[i+K-1]-hh[i];
        ans = ans>tmp?tmp:ans;
    }
    cout<<ans<<endl;

    return 0;
}
