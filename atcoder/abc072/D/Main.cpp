#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

#define MAX 100000

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N, t=0; bool b=false;
    cin>>N;
    for(int i = 1; i <= N; i++){
        int n; cin>>n;
        if(i==n){
            if(b){
                b=false;
            }else{
                b=true; t++;
            }
        } else b=false;
    }
    cout<<t<<endl;
    return 0;
}