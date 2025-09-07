#include <random>
#include <iostream>

int main(){
	std::mt19937 rng{123};
	std::uniform_int_distribution<int> dist(1,6);
	for(int i=0;i<3;++i) std::cout << dist(rng) << " ";
	std::cout << "\n";
}

