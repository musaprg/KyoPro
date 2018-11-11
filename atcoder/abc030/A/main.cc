#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    double A,B,C,D;
    cin>>A>>B>>C>>D;
    double taka = B/A, aoki = D/C;
    if(taka==aoki) cout<<"DRAW"<<endl;
    else if(taka>aoki) cout<<"TAKAHASHI"<<endl;
    else cout<<"AOKI"<<endl;
    return 0;
}
