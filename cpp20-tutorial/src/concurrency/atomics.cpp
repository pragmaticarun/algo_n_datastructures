#include <atomic>
#include <thread>
#include <iostream>

std::atomic<int> counter{0};

int main(){
	std::thread t1([]{ for(int i=0;i<10000;++i) counter.fetch_add(1, std::memory_order_relaxed); });
	std::thread t2([]{ for(int i=0;i<10000;++i) counter.fetch_add(1, std::memory_order_relaxed); });
	t1.join(); t2.join();
	std::cout<<counter.load()<<"\n";
}

