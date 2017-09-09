#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    set<int> st;
    for(int i = 0; i < N; i++){
        int a; cin>>a;
        if(st.count(a) == 0) st.insert(a);
        else st.erase(a);
    }
    cout<<st.size()<<endl;
    return 0;
}