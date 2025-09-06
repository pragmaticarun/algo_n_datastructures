#include <chrono>
#include <iostream>
#include <stop_token>
#include <thread>

using namespace std::chrono_literals;

int main() {
	std::cout << "jthread and stop_token example\n";

	std::jthread worker([](std::stop_token st){
		int iteration = 0;
		while (!st.stop_requested()) {
			std::cout << "working... iteration " << iteration++ << "\n";
			std::this_thread::sleep_for(200ms);
		}
		std::cout << "stop requested, exiting thread\n";
	});

	std::this_thread::sleep_for(900ms);
	std::cout << "requesting stop\n";
	worker.request_stop();
	return 0;
}

