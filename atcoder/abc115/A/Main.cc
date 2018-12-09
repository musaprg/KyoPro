#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    if(N==25) cout<<"Christmas"<<endl;
    else if(N==24) cout<<"Christmas Eve"<<endl;
    else if(N==23) cout<<"Christmas Eve Eve"<<endl;
    else if(N==22) cout<<"Christmas Eve Eve Eve"<<endl;
    return 0;
}
