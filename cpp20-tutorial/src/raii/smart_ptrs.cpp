#include <memory>
#include <iostream>

struct X { int v; X(int v):v(v){} ~X(){ std::cout<<"~X\n"; } };

int main(){
	auto up = std::make_unique<X>(42);
	{ auto sp = std::make_shared<X>(7); auto sp2 = sp; std::cout<<sp.use_count()<<"\n"; }
	std::cout << up->v << "\n";
}
