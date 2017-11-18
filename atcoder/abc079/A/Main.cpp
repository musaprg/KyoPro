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
    int N; cin>>N;
    int a = N/1000, b = (N%1000)/100, c = (N%100)/10, d = N%10;
    cout << (((a==b&&b==c)||(b==c&&c==d)) ? "Yes" : "No") << endl;
    return 0;
}