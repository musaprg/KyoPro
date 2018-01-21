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
#define maxN 100000

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,x=0,y=0,t=0,cx=0,cy=0,ct=0;
    cin>>N;
    for(int i = 0; i < N; i++){
        cin>>t>>x>>y;
        if((t-ct)<(abs(cx-x)+abs(cy-y)) || (t-ct-abs(cx-x)-abs(cy-y))%2!=0){
            cout<<"No"<<endl;
            return 0;
        }
        cx=x; cy=y; ct=t;
    }
    cout<<"Yes"<<endl;
    return 0;
}