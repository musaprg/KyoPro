#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#define INF (2<<29)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    int n[4];
    for(int i = 0; i < 4; i++){
        n[i] = 0;
    }
    string num;
    cin>>num;
    for(int i = 0; i < N; i++){
        n[(num[i]-'0')-1]++;
    }
    int mx=0,mn=INF,mxn,mnn;
    for(int i = 0; i < 4; i++){
        if(n[i]>mx){
            mx=n[i]; mxn=i;
        }
        if(n[i]<mn){
            mn=n[i]; mnn=i;
        }
    }
    cout<<mx<<" "<<mn<<endl;
    return 0;
}