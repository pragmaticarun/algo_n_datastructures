#include <mutex>
#include <condition_variable>
#include <queue>
#include <thread>
#include <iostream>

std::mutex m; std::condition_variable cv; std::queue<int> q; bool done=false;

void producer(){ for(int i=0;i<5;++i){ { std::unique_lock lk(m); q.push(i); } cv.notify_one(); } { std::lock_guard lk(m); done=true; } cv.notify_all(); }
void consumer(){ for(;;){ std::unique_lock lk(m); cv.wait(lk,[]{ return !q.empty() || done; }); if(!q.empty()){ std::cout<<q.front()<<" "; q.pop(); } else if(done) break; } std::cout<<"\n"; }

int main(){ std::thread p{producer}, c{consumer}; p.join(); c.join(); }

