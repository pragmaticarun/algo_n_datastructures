#include <system_error>
#include <fstream>
#include <string>
#include <iostream>

std::error_code read_text(const std::string& path, std::string& out) noexcept {
	std::ifstream f(path);
	if(!f) return std::make_error_code(std::errc::no_such_file_or_directory);
	out.assign((std::istreambuf_iterator<char>(f)), {});
	return {};
}

int main(){ std::string s; auto ec = read_text("/no/such", s); if(ec) std::cout<<ec.message()<<"\n"; }

