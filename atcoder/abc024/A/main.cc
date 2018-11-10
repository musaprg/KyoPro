#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int A,B,C,K,S,T;
    cin>>A>>B>>C>>K>>S>>T;
    int ST = S+T;
    cout<<(S*A+T*B-ST*((ST>=K)?C:0))<<endl;
    return 0;
}
