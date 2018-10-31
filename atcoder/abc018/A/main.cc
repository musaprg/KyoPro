#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int nums[3];
    vector<int> ans;
    for(int i = 0; i < 3; i++)
        cin>>nums[i];
    for(int i = 0; i < 3; i++){
        int ans;
        ans = (nums[i]>nums[(i+1)%3]?1:0) + (nums[i]>nums[(i+2)%3]?1:0);
        cout<<3-ans%3<<endl;
    }

    return 0;
}
