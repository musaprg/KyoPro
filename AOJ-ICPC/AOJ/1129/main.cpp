#include <iostream>
#include <cstdlib>
#include <queue>
#define INF (2<<29)
using namespace std;

typedef struct _node {
    _node* next;
    int n;
} Node;

Node* h;
int n,r,p,c;

Node* initNode(){
    Node* head = (Node*)malloc(sizeof(Node));
    head->n = n;
    Node* bef;
    bef = head;
    for(int i = n-1; i >= 1; i--){
        Node* tmp = (Node*)malloc(sizeof(Node));
        tmp->n = i;
        bef->next = tmp;
        bef = tmp;
    }
    return head;
}

// void freeNode(Node* n){
//     if(n->next != NULL) freeNode(n->next);
//     free(n);
// }

void pc(){
    Node *n1,*n2,*n3,*n4;
    // cout<<"[INFO]SHUFFLE-BEGIN"<<endl;
    if(p==1 && c==n) return;
    n1 = h;
    for(int i = 0; i < p-2; i++){ //p-1番目=n1
        n1 = n1->next;
    }
    n2 = n1->next; //p番目=n2
    
    // cout<<"p = "<<n2->n<<endl;
    
    n3 = n1;
    for(int i = 0; i < c; i++){ //p+c番目=n3
        n3 = n3->next;
        // cout<<"hoge"<<endl;
    }
    n4 = n3->next;
    n1->next = n4;
    n3->next = h;
    h = n2; //headをn2に
    // cout<<"[INFO]SHUFFLE-END"<<endl;
}

int main(void){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    for(;;){
        cin>>n>>r;
        if(n==0 && r==0) break;
        h = initNode();
        for(int i = 0; i < r; i++){
            cin>>p>>c;
            // cout << "p=" << p << ",c=" << c << endl;
            pc();
        }
        cout<<h->n<<endl;
        // cout<<"ほげ"<<endl;
    }

    return 0;
}