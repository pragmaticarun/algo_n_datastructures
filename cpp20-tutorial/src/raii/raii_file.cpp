#include <cstdio>
#include <stdexcept>
#include <utility>

class File {
	std::FILE* f;
public:
	explicit File(const char* path, const char* mode) : f(std::fopen(path, mode)) {
		if (!f) throw std::runtime_error("open failed");
	}
	~File(){ if (f) std::fclose(f); }
	File(const File&) = delete;
	File& operator=(const File&) = delete;
	File(File&& o) noexcept : f(std::exchange(o.f,nullptr)) {}
	File& operator=(File&& o) noexcept { if (this!=&o){ if(f) std::fclose(f); f=std::exchange(o.f,nullptr);} return *this; }
	std::FILE* get() const { return f; }
};

int main(){
	try { File f{"/dev/null", "w"}; (void)f.get(); }
	catch(const std::exception& e){ std::fprintf(stderr, "%s\n", e.what()); }
}
