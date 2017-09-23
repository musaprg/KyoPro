#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,M,K; cin>>N>>M>>K;
    ll NM = N*M;
    if(K<=NM){
        if(K%N==0||K%M==0) cout<<"Yes"<<endl;
        else{
            int tmp = K + K%N;
            // cout<<"tmp is "<<tmp<<endl;
            int t = tmp/M;
            int ans = 0;
            for(int i = 1; i <= M; i++){
                ans = tmp+i*(N-2*t);
                // cout<<"t is "<<t<<endl;
                // cout<<"target is "<<tmp+i*(N-2*t)<<endl;
                if(ans==K){
                    cout<<"Yes"<<endl;
                    ans=-1; break;
                }
            }
            if(ans!=-1) cout<<"No"<<endl;
        }
    }else cout<<"No"<<endl;
    return 0;
}