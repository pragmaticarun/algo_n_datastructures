#include <algorithm>
#include <concepts>
#include <ranges>
#include <vector>

template <std::ranges::random_access_range R>
requires std::sortable<std::ranges::iterator_t<R>>
void sort_in_place(R&& r) { std::ranges::sort(r); }

int main(){
	std::vector<int> v{3,1,4,1,5};
	sort_in_place(v);
	return v[0]==1 && v[1]==1 ? 0 : 1;
}
