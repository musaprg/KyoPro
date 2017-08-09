#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int X,Y; cin>>X>>Y;
    cout<<(X>Y?X:Y)<<endl;
    return 0;
}