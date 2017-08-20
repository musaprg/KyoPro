#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int x,a,b;
    cin>>x>>a>>b;
    cout<<(abs(x-a)<abs(x-b) ? 'A' : 'B')<<endl;
    return 0;
}