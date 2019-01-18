#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll N,K;
    cin>>N>>K;
    vector<ll> hh;
    vector<ll> ans;
    for(ll i = 0; i < N; i++){
        ll tmp;
        cin>>tmp;
        hh.emplace_back(tmp);
    }
    sort(hh.begin(), hh.end());

    for(ll i = 0; i < N-K+1; i++){
        ans.emplace_back(hh[i+K-1]-hh[i]);
    }
    sort(ans.begin(), ans.end());
    cout<<ans[0]<<endl;

    return 0;
}
