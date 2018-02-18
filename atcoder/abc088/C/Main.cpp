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
    int c[3][3];
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cin>>c[i][j];
        }
    }
    int count = 0;
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            if(c[i][j]-c[i+1][j]==c[i][j+1]-c[i+1][j+1]) count++;
        }
    }
    cout<<(count==4?"Yes":"No")<<endl;
    return 0;
}