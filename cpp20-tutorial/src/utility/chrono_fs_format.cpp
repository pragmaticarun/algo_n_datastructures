#include <chrono>
#include <filesystem>
#include <format>
#include <iostream>

int main(){
	namespace fs = std::filesystem;
	auto now = std::chrono::system_clock::now();
	fs::path p = fs::current_path();
	std::cout << std::format("path={}\n", p.string());
	std::cout << std::format(
		"epoch={}\n",
		std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count());
}

