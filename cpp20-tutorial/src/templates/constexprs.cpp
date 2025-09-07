#include <bit>
#include <cstdint>
#include <iostream>

constexpr int square(int x){ return x*x; }
consteval int add1(int x){ return x+1; }
constinit std::uint32_t glob = 5u;

int main(){
	static_assert(square(3)==9);
	constexpr int y = add1(4); (void)y;
	glob = std::rotl(glob, 1);
	std::cout << glob << "\n";
}
