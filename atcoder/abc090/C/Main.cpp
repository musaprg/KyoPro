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
// #define maximum 1000000000

using namespace std;

int N,M;

int calc(int n, int m){
    int count = 0;
    if(n-1>=0){
        if(m<=0)
    }

    return count%2==0?0:1;
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>M;
    int ans = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            ans += calc(i,j);
            cout<<ans<<endl;
        }
    }
    cout<<ans<<endl;
    return 0;
}