#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <iostream>

int main(){
	std::vector<int> v{5,2,4,1,3};
	std::ranges::sort(v);
	std::map<int,const char*> m{{1,"one"},{2,"two"}};
	std::unordered_map<int,int> um{{1,10},{2,20}};
	std::cout << v.front() << "," << m[2] << "," << um[1] << "\n";
}
