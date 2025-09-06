#include <iostream>
#include <string>
#include <type_traits>

consteval int square_consteval(int value) { return value * value; }

constinit int global_counter = 0;

auto concat(auto a, auto b) {
	return a + b;
}

auto multiply(auto a, auto b) requires std::integral<decltype(a * b)> {
	return a * b;
}

int main() {
	std::cout << "consteval/constinit/abbreviated templates example\n";

	constexpr int nine = square_consteval(3);
	static_assert(nine == 9);
	std::cout << "square_consteval(3) = " << nine << "\n";

	std::cout << "global_counter = " << global_counter << "\n";
	global_counter += 5;
	std::cout << "global_counter (after) = " << global_counter << "\n";

	std::cout << concat(std::string{"Hello "}, std::string{"C++20"}) << "\n";
	std::cout << multiply(6, 7) << "\n";
	return 0;
}

