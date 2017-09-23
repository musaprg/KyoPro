#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,M,K; cin>>N>>M>>K;
    bool f=false;
    for(int i = 0; i <= N; i++){
        for(int j = 0; j <= M; j++){
            if(M*i+N*j-2*i*j==K){ f=true; break; }
        }
    }
    cout<<(f?"Yes":"No")<<endl;
    return 0;
}