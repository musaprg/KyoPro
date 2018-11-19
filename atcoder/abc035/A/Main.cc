#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int W,H; cin>>W>>H;
    if(W%16==0){
        if(H%9==0) cout<<"16:9"<<endl;
        else cout<<"4:3"<<endl;
    }else cout<<"4:3"<<endl;
    return 0;
}
