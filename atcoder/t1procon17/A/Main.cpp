#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a = 0;
    for(int i = 0; i < 6; i++){
        char c = getchar();
        if(c-'0'==1) a++;
    }
    cout<<a<<endl;
    return 0;
}