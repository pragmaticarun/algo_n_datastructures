// Build: g++ -std=c++17 -O2 -Wall -Wextra map_pitfalls.cpp -o map_pitfalls
#include <iostream>
#include <map>
#include <unordered_map>
#include <string>

using std::cout;
using std::endl;
using std::map;
using std::string;
using std::unordered_map;

// 1) Pitfall: operator[] inserts a default-constructed value if key is absent
static void demo_unintended_insertion() {
    cout << "\n=== 1) operator[] causes unintended insertion ===\n";
    map<string, int> wordCounts;

    // Accessing a missing key inserts it with value 0
    int count = wordCounts["missing"];  // inserts {"missing", 0}
    cout << "count of 'missing' after operator[] access: " << count << "\n";
    cout << "size after access: " << wordCounts.size() << "\n";

    // Safer: use find() when you don't want insertion
    auto it = wordCounts.find("another");
    if (it == wordCounts.end()) {
        cout << "'another' not present and not inserted. size: " << wordCounts.size() << "\n";
    }

    // Note: operator[] is not available on const map (by design)
    // const map<string,int> cm; int x = cm["k"]; // does not compile
}

// 2) Pitfall: at() does not insert; it throws on missing key
static void demo_at_vs_find() {
    cout << "\n=== 2) at() throws on missing key ===\n";
    map<string, int> config{{"threads", 8}};

    try {
        cout << "threads: " << config.at("threads") << "\n";
        cout << "attempting to read 'timeout' using at()...\n";
        cout << config.at("timeout") << "\n"; // throws std::out_of_range
    } catch (const std::out_of_range& e) {
        cout << "caught std::out_of_range: " << e.what() << "\n";
    }

    // Prefer find() when key may be absent and you don't want exceptions
    if (auto it = config.find("timeout"); it != config.end()) {
        cout << "timeout: " << it->second << "\n";
    } else {
        cout << "timeout missing; use a default or insert explicitly\n";
    }
}

// 3) Pitfall: Erasing while iterating incorrectly
static void demo_erase_while_iterating() {
    cout << "\n=== 3) erasing while iterating ===\n";
    map<int, int> numbers{{1,1},{2,4},{3,9},{4,16},{5,25}};

    cout << "original keys: ";
    for (const auto& kv : numbers) cout << kv.first << ' ';
    cout << "\n";

    // Incorrect (dangerous): erasing by key inside range-for while iterating the same container
    // for (const auto& kv : numbers) {
    //     if (kv.first % 2 == 0) numbers.erase(kv.first); // invalidates iteration state
    // }

    // Correct: use iterator loop and use the returned iterator from erase
    for (auto it = numbers.begin(); it != numbers.end(); ) {
        if (it->first % 2 == 0) {
            it = numbers.erase(it); // safe: returns next iterator
        } else {
            ++it;
        }
    }

    cout << "after erasing even keys: ";
    for (const auto& kv : numbers) cout << kv.first << ' ';
    cout << "\n";
}

// 4) Pitfall: Assuming insertion order; std::map is ordered by key
static void demo_ordering_assumption() {
    cout << "\n=== 4) ordering assumption ===\n";
    map<int, string> m{{42, "forty-two"}, {7, "seven"}, {100, "hundred"}};
    cout << "iteration order (sorted by key):\n";
    for (const auto& [k, v] : m) cout << k << " -> " << v << "\n";

    cout << "note: order is by key, not insertion time.\n";
}

// 5) Pitfall: Trying to modify a key in-place
// Keys in map are const within the element; changing a key breaks ordering.
// Correct approach: erase+insert, or C++17 node handle to modify key.
static void demo_modify_key_with_extract() {
    cout << "\n=== 5) modifying a key (use extract in C++17) ===\n";
    map<string, int> m{{"alpha", 1}, {"beta", 2}};

    // Wrong (won't compile): m.begin()->first = "gamma"; // key is const

    // Safe approach using node handle
    auto node = m.extract("alpha");
    if (!node.empty()) {
        node.key() = "gamma"; // modify key outside the tree
        m.insert(std::move(node));
    }

    for (const auto& [k, v] : m) cout << k << " -> " << v << "\n";
}

// 6) Pitfall: Custom comparator that defines key equivalence unexpectedly
// Example: compare only by string length. Distinct strings of same length are considered equivalent.
struct ByLengthOnly {
    bool operator()(const string& a, const string& b) const {
        return a.size() < b.size();
    }
};

struct ByLengthThenLex {
    bool operator()(const string& a, const string& b) const {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    }
};

static void demo_custom_comparator_pitfall() {
    cout << "\n=== 6) comparator defines equivalence unexpectedly ===\n";
    map<string, int, ByLengthOnly> bad{{"aa", 1}};
    bad.insert({"bb", 2}); // treated as equivalent to "aa" (same length)
    bad.insert({"ccc", 3});
    bad.insert({"ddd", 4}); // equivalent to "ccc"

    cout << "ByLengthOnly map contents (one per length):\n";
    for (const auto& [k, v] : bad) cout << k << " -> " << v << "\n";

    map<string, int, ByLengthThenLex> good{{"aa", 1}};
    good.insert({"bb", 2});
    good.insert({"ccc", 3});
    good.insert({"ddd", 4});
    cout << "ByLengthThenLex map contents (no unintended equivalence):\n";
    for (const auto& [k, v] : good) cout << k << " -> " << v << "\n";
}

// 7) Pitfall: Double lookup patterns; prefer insert/try_emplace
static void demo_insert_patterns() {
    cout << "\n=== 7) avoid double lookups ===\n";
    map<string, int> counts;

    // Less efficient pattern: find then operator[] or insert
    if (counts.find("apple") == counts.end()) {
        counts["apple"] = 1; // find + insert + lookup again
    }

    // Better: single operation insert
    auto [it, inserted] = counts.insert({"banana", 1});
    cout << "banana inserted: " << std::boolalpha << inserted << "\n";

    // Best when constructing in place (avoids temporary pair)
    auto [it2, inserted2] = counts.try_emplace("cherry", 1);
    cout << "cherry inserted: " << inserted2 << "\n";

    // Updating without accidental insertion: use find
    if (auto it3 = counts.find("durian"); it3 != counts.end()) {
        it3->second += 1;
    } else {
        cout << "durian not present; not inserted implicitly.\n";
    }
}

// 8) Pitfall: Holding references/iterators across erases
static void demo_dangling_references_warning() {
    cout << "\n=== 8) dangling references after erase ===\n";
    map<int, string> m{{1, "one"}, {2, "two"}};
    auto it = m.find(1);
    const string& ref = it->second; // reference valid as long as element exists
    cout << "ref before erase: " << ref << "\n";

    m.erase(1); // invalidates iterators/references to the erased element
    // Using 'ref' here would be undefined behavior. Avoid keeping dangling refs.
    cout << "erased key 1; any references/iterators to that element are now invalid.\n";
}

int main() {
    cout << "Demonstrating common std::map pitfalls and safer alternatives\n";
    demo_unintended_insertion();
    demo_at_vs_find();
    demo_erase_while_iterating();
    demo_ordering_assumption();
    demo_modify_key_with_extract();
    demo_custom_comparator_pitfall();
    demo_insert_patterns();
    demo_dangling_references_warning();

    cout << "\nDone.\n";
    return 0;
}

