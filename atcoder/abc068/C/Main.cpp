#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int N,M;
bool e_flg=false;
// vector<vector<int> > ED;

// void dfs(int n, int c){
//     if(e_flg) return;
//     if(c<2 && n==N) return;
//     if(c==2){
//         if(n==N){
//             cout<<"POSSIBLE"<<endl;
//             e_flg=true;
//         }
//         return;
//     }
//     for(int i = 1; i <= N; i++){
//         if(i==n) continue;
//         vector<int>::iterator ni = find(ED[n].begin(),ED[n].end(),i);
//         if(ni!=ED[n].end()) dfs(i,c+1);
//     }
// }

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>M;
    vector<int> ap;
    set<int> bp;
    // for(int i = 0; i <= N; i++){
    //     vector<int> v;
    //     ED.push_back(v);
    // }
    for(int i = 0; i < M; i++){
        int a,b;
        cin>>a>>b;
        if(a==1){
            ap.push_back(b);
            continue;
        }
        if(b==N){
            bp.insert(a);
            continue;
        }
        
        // ED[a].push_back(b);
    }
    // dfs(1,0);
    // if(e_flg==false) cout<<"IMPOSSIBLE"<<endl;
    for(int i = 0; i < ap.size(); i++){
        if(bp.find(ap[i]) != bp.end()){
            cout<<"POSSIBLE"<<endl;
            return 0;
        }
    }
    cout<<"IMPOSSIBLE"<<endl;
    return 0;
}