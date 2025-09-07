#include <span>
#include <string_view>
#include <iostream>

int sum(std::span<const int> xs) {
	int s = 0;
	for (int x : xs) s += x;
	return s;
}

void greet(std::string_view name) {
	std::cout << "hi, " << name << "\n";
}

int main() {
	int a[]{1,2,3};
	std::cout << sum(a) << "\n";
	greet("world");
}

