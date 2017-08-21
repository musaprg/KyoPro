#include <iostream>
#include <vector>
#include <algorithm>
#define swap(A,B) {int tmp = A; A = B; B = tmp;}

using namespace std;

int nums[] = {1, 2, 3, 4, 5, 6};

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    for(int i = 0; i < N; i++){
        swap(nums[i%5], nums[i%5+1]);
    }
    for(int i = 0; i < 6; i++){
        cout<<nums[i];
    }
    cout<<endl;
    return 0;
}