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
    int a,b,c,x,y; cin>>a>>b>>c>>x>>y;
    int ans = 0;
    cout<<min(
        a*x+b*y,
        min(
            c*2*min(x,y) + (x>y?a:b)*(max(x,y)-min(x,y)),
            c*2*max(x,y)
        )
    )<<endl;
    return 0;
}