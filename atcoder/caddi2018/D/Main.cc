#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    bool ans = true;
    for(int i = 0; i < N; i++){
        int a;
        cin>>a;
        ans = ans & (a % 2 == 0);
    }
    cout<<(ans?"second":"first")<<endl;
    return 0;
}
