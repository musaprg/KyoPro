#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void){
	std::cin.tie(0);
	std::ios::sync_with_stdio(false);
	
	int N, T, tmp;
	vector<int> t;

	cin>>N>>T;
	for(int i = 0; i < N; i++){
		cin>>tmp;
		t.push_back(tmp);
	}

	vector<int>::iterator it = t.begin();
	vector<int>::iterator endIt = t.end();
	int sum = 0;
	int diff = *it-*(it-1);
	it++;
	while(it != endIt){
		if((diff=*it-*(it-1))<=T) 	sum += diff;
		else						sum += T;
		it++;
	}
	sum+=T;
	
	cout << sum << endl;


	
	return 0;
}
