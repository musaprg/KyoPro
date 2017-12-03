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
    ll N,n,a=0;
    cin>>N;
    n = N;
    while(n%10 != 0){
        a += n % 10;
        n /= 10;
    }
    cout<<((N%a==0)?"Yes":"No")<<endl;
    return 0;
}