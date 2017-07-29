//
//  main.cpp
//  gc011
//
//  Created by Lugi on 2017/03/12.
//  Copyright © 2017年 musa. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int N, C, K;

int main(int argc, const char * argv[]) {
    cin>>N>>C>>K;
    int bus = 1;
    int cur = 0;
    int hito = 0;
    vector<int> T(N);
    for(int i=0; i<N; i++){
        cin >> T[i];
        if(C>hito){
            if(T[cur]+K<T[i]){
                bus++;
                cur=i;
            }else{
                hito++;
            }
        }else{
            bus++;
            cur=i+1;
        }
    }
    cout<<bus<<endl;
    
    return 0;
}
