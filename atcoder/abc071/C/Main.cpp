#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    vector<int> in;
    vector<int> num;
    for(int i = 0; i < N; i++){
        int n; cin>>n; in.push_back(n);
    }
    sort(in.begin(), in.end());
    for(int i = N-1; i > 0; i--){
        if(in[i] == in[i-1]){
            num.push_back(in[i]);
            i--;
        }
        if(num.size() == 2) break;
    }
    // for(auto itr = in.rbegin(); itr != in.rend(); itr++) {
    //     if(*itr == *(itr+1)){
    //         num.push_back(*itr);
    //         itr++;
    //         continue;
    //     }
    //     if(num.size() == 2) break;
    // }
    
    if(num.size() < 2) cout<<0<<endl;
    else{
        ll a = num[0];
        ll b = num[1];
        cout<<a*b<<endl;
    }
    return 0;
}