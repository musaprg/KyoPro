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
    for(;;){
        int n,m; cin>>n>>m;
        bool cont = true;
        if(n==0&&m==0) break;
        int taro[100],hanako[100],tarosum=0,hanakosum=0;
        for(int i = 0; i < n; i++){
            cin>>taro[i];
            tarosum+=taro[i];
        }
        for(int i = 0; i < m; i++){
            cin>>hanako[i];
            hanakosum+=hanako[i];
        }
        for(int i = 0; i < n && cont; i++){
            for(int j = 0; j < m && cont; j++){
                if(tarosum+2*hanako[j]==hanakosum+2*taro[i]){
                    printf("%d %d\n", taro[i], hanako[j]);
                    cont = false;
                }
            }
        }
        if(cont) cout<<"-1"<<endl;
    }
    return 0;
}