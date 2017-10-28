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
    int N,K; cin>>N>>K;
    int ans = 1;
    for(int i = 0; i < N; i++)
        ans = min(ans*2,ans+K);
    cout<<ans<<endl;
    return 0;
}