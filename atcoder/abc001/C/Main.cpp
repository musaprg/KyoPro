#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    double deg, dis; cin>>deg>>dis; deg/=10; dis/=60;
    char ans[] = {'C', 'N', 'E', 'W', 'S'};
    dis*=10; dis+=0.5; dis=int(dis); dis/=10; //四捨五入
    int w;
    if(0.0<=dis&&dis<=0.2) w=0;
    else if(0.3<=dis&&dis<=1.5) w=1;
    else if(1.6<=dis&&dis<=3.3) w=2;
    else if(3.4<=dis&&dis<=5.4) w=3;
    else if(5.5<=dis&&dis<=7.9) w=4;
    else if(8.0<=dis&&dis<=10.7) w=5;
    else if(10.8<=dis&&dis<=13.8) w=6;
    else if(13.9<=dis&&dis<=17.1) w=7;
    else if(17.2<=dis&&dis<=20.7) w=8;
    else if(20.8<=dis&&dis<=24.4) w=9;
    else if(24.5<=dis&&dis<=28.4) w=10;
    else if(28.5<=dis&&dis<=32.6) w=11;
    else w=12;
    string dir;
    if(w==0) dir="C";
    else if(11.25<=deg&&deg<33.75) dir="NNE";
    else if(33.75<=deg&&deg<56.25) dir="NE";
    else if(56.25<=deg&&deg<78.75) dir="ENE";
    else if(78.75<=deg&&deg<101.25) dir="E";
    else if(101.25<=deg&&deg<123.75) dir="ESE";
    else if(123.75<=deg&&deg<146.25) dir="SE";
    else if(146.25<=deg&&deg<168.75) dir="SSE";
    else if(168.75<=deg&&deg<191.25) dir="S";
    else if(191.25<=deg&&deg<213.75) dir="SSW";
    else if(213.75<=deg&&deg<236.25) dir="SW";
    else if(236.25<=deg&&deg<258.75) dir="WSW";
    else if(258.75<=deg&&deg<281.25) dir="W";
    else if(281.25<=deg&&deg<303.75) dir="WNW";
    else if(303.75<=deg&&deg<326.25) dir="NW";
    else if(326.25<=deg&&deg<348.75) dir="NNW";
    else dir="N";
    cout<<dir<<" "<<w<<endl;
    return 0;
}