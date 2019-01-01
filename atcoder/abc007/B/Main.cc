#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string A;
    cin>>A;
    if(A.size() > 1){
        cout<<A.substr(0,A.size()-1)<<endl;
    }else if(A!="a"){
        cout<<(char)(A.c_str()[0]-1)<<endl;
    }else{
        cout<<"-1"<<endl;
    }
    return 0;
}
