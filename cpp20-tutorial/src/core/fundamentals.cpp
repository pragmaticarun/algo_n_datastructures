#include <iostream>
#include <string>

// Demonstrates value categories, initialization, references, and move
std::string make_string() { return std::string{"hello"}; }
void take_lvalue(const std::string& s) { std::cout << "lvalue:" << s << "\n"; }
void take_rvalue(std::string&& s) { std::cout << "rvalue:" << s << "\n"; }

int main() {
	std::string a{};                // value-init
	std::string b{"world"};        // direct list-init

	a = make_string();              // move elision / NRVO
	take_lvalue(a);                 // binds as lvalue
	take_rvalue(std::move(a));      // explicit move -> xvalue

	int x{42};                      // no narrowing
	int y = 7;
	int& ref = y;                   // lvalue reference
	const int& cref = x + y;        // binds to temporary
	std::cout << ref << "," << cref << "\n";
}
