#include <iostream>
#include <string>
#include <string_view>

// Lifetime pitfalls and string_view
std::string_view bad() {
	std::string s = "temp";
	return std::string_view{s}; // dangling! demonstration only
}

std::string_view good(const std::string& s) { return std::string_view{s}; }

int main(){
	std::string owned = "owned text";
	auto sv = good(owned);
	std::cout << sv << "\n";
	// Do not use: auto d = bad(); // would dangle
}
