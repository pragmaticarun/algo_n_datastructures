#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <source_location>
#include <span>
#include <vector>

void log_with_location(const std::string& message,
                       const std::source_location location = std::source_location::current()) {
	std::cout << location.file_name() << ":" << location.line() << " in "
			  << location.function_name() << ": " << message << "\n";
}

int sum_span(std::span<const int> values) {
	return std::accumulate(values.begin(), values.end(), 0);
}

int main() {
	std::cout << "span/bit_cast/source_location example\n";

	std::vector<int> data{1,2,3,4,5};
	std::span<const int> view{data};
	std::cout << "sum = " << sum_span(view) << "\n";

	float f = 3.1415926f;
	std::uint32_t as_bits = std::bit_cast<std::uint32_t>(f);
	std::cout << "float bits = 0x" << std::hex << as_bits << std::dec << "\n";

	log_with_location("Hello from source_location");
	return 0;
}

