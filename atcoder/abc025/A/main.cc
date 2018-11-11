#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string S;
    int N,count=1;
    bool bContinueFlag = true;
    cin>>S>>N;
    for(int i = 0; i < S.size() && bContinueFlag; ++i){
        for(int j = 0; j < S.size() && bContinueFlag; ++j){
            if(count==N){
                cout<<S[i]<<S[j]<<endl;
                bContinueFlag = false;
            } else ++count; 
        }
    }
    return 0;
}
