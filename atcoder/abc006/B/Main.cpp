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
#define maxN 1000000

using namespace std;

ll dp[maxN+1];

ll a(ll n){
    if (dp[n] != -1) return dp[n];
    if (n == 1) return dp[n] = 0;
    if (n == 2) return dp[n] = 0;
    if (n == 3) return dp[n] = 1;
    else return dp[n] = a(n-1)%10007 + a(n-2)%10007 + a(n-3)%10007;
}

int main(void){
    cin.sync_with_stdio(false);
    ll n; cin>>n;
    for(ll i = 0; i < maxN+1; i++){
        dp[i] = -1;
    }
    cout<<a(n)%10007<<endl;
    return 0;
}