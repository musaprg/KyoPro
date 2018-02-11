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

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll x,k; cin>>x>>k;
    ll base = pow(10,k);

    if (x < base) {
        cout<<base<<endl;
    } else {
        ll ans = base;
        while (x >= ans) {
            ans += base;
        }
        cout<<ans<<endl;
    }
    return 0;
}