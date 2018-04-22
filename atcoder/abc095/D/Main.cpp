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
    int N,C; cin>>N>>C;
    vector<int> x,v;
    for(int i = 0; i < N; i++){
        int a,b; cin>>a>>b;
        x.push_back(a);
        v.push_back(b);
    }
    
    return 0;
}