#include <coroutine>
#include <exception>
#include <iostream>
#include <memory>
#include <optional>

template <typename T>
class Generator {
public:
	struct promise_type {
		T current_value{};
		std::exception_ptr exception{};

		Generator get_return_object() {
			return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};
		}
		std::suspend_always initial_suspend() noexcept { return {}; }
		std::suspend_always final_suspend() noexcept { return {}; }
		std::suspend_always yield_value(T value) noexcept {
			current_value = std::move(value);
			return {};
		}
		void return_void() {}
		void unhandled_exception() { exception = std::current_exception(); }
	};

	using handle_type = std::coroutine_handle<promise_type>;

	explicit Generator(handle_type handle) : handle_(handle) {}
	Generator(const Generator&) = delete;
	Generator(Generator&& other) noexcept : handle_(other.handle_) { other.handle_ = {}; }
	~Generator() { if (handle_) handle_.destroy(); }

	bool move_next() {
		if (!handle_ || handle_.done()) return false;
		handle_.resume();
		if (handle_.promise().exception) std::rethrow_exception(handle_.promise().exception);
		return !handle_.done();
	}

	T current_value() const { return handle_.promise().current_value; }

private:
	handle_type handle_{};
};

Generator<int> iota(int start, int count) {
	for (int i = 0; i < count; ++i) {
		co_yield start + i;
	}
}

int main() {
	std::cout << "Coroutines generator example\n";
	auto gen = iota(10, 5);
	while (gen.move_next()) {
		std::cout << gen.current_value() << " ";
	}
	std::cout << "\n";
	return 0;
}

