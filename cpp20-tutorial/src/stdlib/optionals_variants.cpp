#include <optional>
#include <variant>
#include <iostream>

std::optional<int> maybe_parse(bool ok) {
	if (ok) return 42;
	return std::nullopt;
}

using V = std::variant<int, double>;

int main() {
	if (auto v = maybe_parse(true)) std::cout << *v << "\n";
	V v{3.14};
	std::visit([](auto&& x){ std::cout << x << "\n"; }, v);
}

