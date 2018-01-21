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
    string a,b; cin>>a>>b;
    double res = sqrt(stoi(a+b));
    cout<<(modf(res, &res)==0?"Yes":"No")<<endl;
    
    return 0;
}