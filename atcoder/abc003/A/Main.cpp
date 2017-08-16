#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    int sum = 0;
    for(int i = 1; i <= N; i++){
        sum += i*10000;
    }
    sum /= N;
    cout<<sum<<endl;
    return 0;
}