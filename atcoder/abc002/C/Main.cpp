#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    double x[3],y[3],a,b,c,d;
    for(int i = 0; i < 3; i++){
        cin>>x[i]>>y[i];
    }
    a = x[2]-x[0];
    b = y[2]-y[0];
    c = x[1]-x[0];
    d = y[1]-y[0];
    double res = fabs(a*d-b*c)/2.0;
    printf("%.1f\n", res);
    return 0;
}