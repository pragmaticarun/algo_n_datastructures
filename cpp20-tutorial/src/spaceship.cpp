#include <compare>
#include <iostream>
#include <set>
#include <string>
#include <vector>

struct Person {
	std::string name;
	int age{};
	auto operator<=>(const Person&) const = default;
};

int main() {
	std::cout << "Spaceship operator example\n";

	Person a{"Ada", 28};
	Person b{"Bob", 24};
	Person c{"Bob", 24};

	if (a < b) {
		std::cout << a.name << " is ordered before " << b.name << "\n";
	}
	std::cout << std::boolalpha << "b == c? " << (b == c) << "\n";

	std::set<Person> people{a, b, c};
	for (const auto& p : people) {
		std::cout << p.name << " (" << p.age << ")\n";
	}
	return 0;
}

