#include <stdexcept>
#include <iostream>

int divi(int a, int b){ if(b==0) throw std::runtime_error("divide by zero"); return a/b; }

int main(){
	try{
		std::cout<<divi(4,2)<<"\n";
	}catch(const std::exception& e){
		std::cout<<e.what()<<"\n";
	}
}

