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
#define gr(A,B) s[(A)][(B)+1]
#define gd(A,B) s[(A)+1][(B)]
#define INFTY (1<<21)

using namespace std;

int H,W;
bool s[50+1][50+1]; // isWhite?

bool dfs(int i, int j){
    if(gr(i,j)){
        
    }
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>H>>W;
    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            char c; cin>>c;
            if(c=='.') s[i+1][j+1] = true;
            else s[i+1][j+1] = false;
        }
    }
    // for(int i = 0; i < H; i++){
    //     for(int j = 0; j < W; j++){
    //         char c; cin>>c;
    //         cout<<s[i+1][j+1]<<" ";
    //     }
    //     cout<<endl;
    // }
    
    return 0;
}