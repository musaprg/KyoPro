#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    char tb[16];
    for(int i = 15; i >= 0; i--){
        cin>>tb[i];
    }
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 3; j++){
            cout<<tb[4*i+j]<<" ";
        }
        cout<<tb[4*i+3]<<endl;
    }
    return 0;
}