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
    int N, K; cin>>N>>K;
    int count = 0;
    for(int a = 1; a <= N; a++){
        for(int b = 1; b <= N; b++){
            if(a<b && a<K) continue;
            if(a%b>=K) count++;
        }
    }
    // for(int a = K; a <= N; a++){
    //     count += N-(a+1)+1;
    // }
    // for(int b = K; b <= N; b++){
    //     for(int a = b; a <= N; a++){
    //         if(a%b>=K) count++;
    //     }
    // }
    cout<<count<<endl;
    return 0;
}