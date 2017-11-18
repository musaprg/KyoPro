#include <iostream>
#include <vector> //可変長配列
#include <queue> //キュー
#include <unordered_map> //ハッシュ連想配列
#include <numeric>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define ll long long int
#define INFTY (1<<21)

#define unknown -1

using namespace std;

ll dp[86+1];

ll L(ll n){
    if (n==0) return 2;
    else if (n==1) return 1;
    if(dp[n] != -1) return dp[n];
    return dp[n] = L(n-1) + L(n-2);
}

int main(void){
    cin.sync_with_stdio(false);
    for(int i = 1; i < 86+1; i++){
        dp[i] = -1;
    }
    ll N; cin>>N;
    cout<<L(N)<<endl;
    return 0;
}