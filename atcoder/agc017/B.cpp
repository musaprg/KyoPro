#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int N,A,B,C,D;

int main(void){
    cin.tie(0);
   	ios::sync_with_stdio(false);

    cin>>N>>A>>B>>C>>D;

    q.add(A);

    while(!q.empty()){
        for(i=A+C; i<=A+D; i++){
            q.add(i);
        }
    }

    return 0;
}