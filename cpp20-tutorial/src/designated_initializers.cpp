#include <iostream>
#include <string>

struct Point { int x; int y; };
struct User { int id; std::string name; bool admin; };

int main() {
	std::cout << "Designated initializers example\n";

	Point p{ .x = 10, .y = 20 };
	std::cout << "Point: (" << p.x << ", " << p.y << ")\n";

	User u{ .id = 42, .name = "Alice", .admin = true };
	std::cout << "User: " << u.name << ", id=" << u.id << ", admin=" << std::boolalpha << u.admin << "\n";
	return 0;
}

