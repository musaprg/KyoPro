#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int r;
    cin>>r;
    if(r<2800)
        if(r<1200) cout<<"ABC"<<endl;
        else cout<<"ARC"<<endl;
    else cout<<"AGC"<<endl;
    return 0;
}
