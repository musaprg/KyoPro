#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int T,N,M;
    vector<int> A, B;
    cin>>T>>N;
    for(int i = 0; i < N; i++){
        int a; cin>>a;
        A.push_back(a);
    }
    cin>>M;
    for(int i = 0; i < M; i++){
        int b; cin>>b;
        B.push_back(b);
    }
    int c = 0;
    bool t = true;
    for(int i = 0; i < M; i++){
        
    }
    cout<<(t ? "yes" : "no")<<endl;
    return 0;
}