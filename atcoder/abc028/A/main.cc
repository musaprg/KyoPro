#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    if (N==100) cout<<"Perfect"<<endl;
    else if (N>=60) {
        if (N<90) cout<<"Good"<<endl;
        else cout<<"Great"<<endl;

    } else cout<<"Bad"<<endl;
    return 0;
}
