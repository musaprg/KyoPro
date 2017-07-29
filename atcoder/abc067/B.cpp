#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int N,K,l;
    vector<int> ls;
    cin>>N>>K;
    for(int i = 0; i < N; i++){
        cin>>l;
        ls.push_back(l);
    }
    sort(ls.begin(),ls.end(),greater<int>()); //降順ソート
    int sum=0;
    for(int i = 0; i < K; i++){
        sum+=ls[i];
    }
    cout<<sum<<endl;
    return 0;
}