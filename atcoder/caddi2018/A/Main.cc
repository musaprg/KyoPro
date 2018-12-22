#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string N;
    cin>>N;
    int count = 0;
    for(char c : N){
        if(c=='2') count++;
    }
    cout<<count<<endl;
    return 0;
}
