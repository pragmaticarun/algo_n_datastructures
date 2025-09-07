#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

int main() {
	std::cout << "Ranges pipeline example\n";

	auto numbers = std::views::iota(1, 51);

	auto pipeline = numbers
		| std::views::filter([](int n) { return n % 2 == 0; })
		| std::views::transform([](int n) { return n * n; })
		| std::views::take(10);

	std::vector<int> result;
	for (int value : pipeline) {
		result.push_back(value);
	}

	for (std::size_t i = 0; i < result.size(); ++i) {
		if (i) std::cout << ", ";
		std::cout << result[i];
	}
	std::cout << "\n";
	return 0;
}

