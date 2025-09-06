#include <concepts>
#include <iostream>
#include <string>
#include <type_traits>

template <typename T>
concept Addable = requires(T a, T b) {
	{ a + b } -> std::convertible_to<T>;
};

auto add(Addable auto a, Addable auto b) {
	return a + b;
}

template <typename T>
requires requires(T value) {
	{ value.size() } -> std::convertible_to<std::size_t>;
}
void printSize(const T& value) {
	std::cout << "size: " << value.size() << "\n";
}

int main() {
	std::cout << "Concepts and requires example\n";

	int x = 2, y = 40;
	std::cout << "add(int,int): " << add(x, y) << "\n";

	std::string s1 = "Hello ", s2 = "World";
	std::cout << "add(string,string): " << add(s1, s2) << "\n";

	printSize(std::string{"abc"});
	printSize(std::string{"12345"});

	return 0;
}

