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
    int a,b,c,x,count=0; cin>>a>>b>>c>>x;
    for(int i = 0; i <= a; i++)
        for(int j = 0; j <= b; j++)
            for(int k = 0; k <= c; k++)
                if(x == 500*i+100*j+50*k)
                    count++;
    cout<<count<<endl;
    return 0;
}