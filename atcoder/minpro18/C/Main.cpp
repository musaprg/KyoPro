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
#define maxN 18

using namespace std;

ll rec(){
    
}

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    ll x[maxN+1], c[maxN+1], v[maxN+1];
    bool canbuy[maxN+1];
    for(int i = 1; i <= N; i++)
        canbuy[i] = true;
    for(int i = 1; i <= N; i++)
        cin>>x[i];
    for(int i = 1; i <= N; i++)
        cin>>c[i];
    for(int i = 1; i <= N; i++)
        cin>>v[i];
    
    return 0;
}