#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int
#define AMAX 31000

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    int a[AMAX][2];
    for(int i = 0; i < AMAX; i++){
        a[i][0] = -1;
        a[i][1] = -1;
    }
    cin>>a[1][0]>>a[1][1];
    for(int i = 0; i < N-1; i++){
        int l,r; cin>>l>>r;
        for(int k = 1; k <= AMAX; k++){
            if(a[k][0]==-1){
                a[k][0]=l; a[k][1]=r; break;
            }else{
                if(a[k][0]>r || a[k][1]<l) continue;
                if(a[k][0]>l) a[k][0] = l;
                if(a[k][1]<r) a[k][1] = r;
                break;
            }
        }
    }
    int sum = 0;
    for(int i = 1; a[i][0]!=-1; i++){
        sum+=a[i][1]-a[i][0]+1;
    }
    cout<<sum<<endl;
    return 0;
}