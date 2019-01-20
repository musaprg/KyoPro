#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

void solve(vector<int>& hh, vector<int>::iterator& it){
    auto result = find(it, hh.end(), 0);
    auto res = min_element(it, result);
    for(auto itr = it; itr != result; hh++){
        itr
    }
    if(result == hh.end()) return;
    else solve(hh, ++result);
}


int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    vector<int> hh;
    for(int i = 0; i < N; i++){
        int h;
        cin>>h;
        hh.emplace_back(h);
    }


    return 0;
}
