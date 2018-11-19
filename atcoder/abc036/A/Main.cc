#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int A,B;cin>>A>>B;
    cout<<(B/A+(B%A>0?1:0))<<endl;
    return 0;
}
