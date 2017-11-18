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

int a,b,c,d;

int main(void){
    cin.sync_with_stdio(false);
    a = getchar()-'0';
    b = getchar()-'0';
    c = getchar()-'0';
    d = getchar()-'0';
    getchar();
    int op1[] = {a+b, a-b}, op2[] = {b+c, b-c}, op3[] = {c+d, c-d};
    char op[] = {'+', '-'};
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            for(int k = 0; k < 2; k++){
                if(op1[i]+op2[j]+op3[k]-b-c==7){
                    cout<<a<<op[i]<<b<<op[j]<<c<<op[k]<<d<<"=7"<<endl;
                    return 0;
                }
            }
        }
    }
    return 0;
}