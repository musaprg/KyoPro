#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

#define MAX 100000

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N, a[MAX], r;
    cin>>N;
    for(int i = 0; i < MAX; i++){
        a[i] = 0;
    }
    for(int i = 0; i < N; i++){
        int n; cin>>n;
        a[n]++;
    }
    for(int i = 0; i < MAX-2; i++){
        int tmp = a[i]+a[i+1]+a[i+2];
        if(tmp>r) r = tmp;
    }
    cout<<r<<endl;
    return 0;
}