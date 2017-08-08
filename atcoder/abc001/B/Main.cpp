#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    double m; cin>>m; m/=1000;
    if(m<0.1) m=0;
    else if(0.1<=m && m<=5) m*=10;
    else if(6<=m && m<=30) m+=50;
    else if(35<=m && m<=70) m=(m-30)/5 + 80;
    else m=89;
    if((int)m/10==0) cout<<"0"<<m<<endl;
    else cout<<m<<endl;
    return 0;
}