#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long int

using namespace std;

int b(vector<int> nums, int i){
	nums[i] = nums.back();
	nums.pop_back();
	sort(nums.begin(), nums.end());
	return nums[nums.size() / 2];
}

int main(){
	int n; cin>>n;
	vector<int> nums;
	for(int i = 0; i < n; i++){
		int t; cin>>t;
		nums.push_back(t);
	}
	for(int i = 0; i < n; i++){
		cout<<b(nums, i)<<endl;
	}
	return 0;
}

