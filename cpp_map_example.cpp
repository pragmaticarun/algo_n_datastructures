#include <iostream>
#include <map>
#include <string>

using std::cout;
using std::endl;

void printPhoneBook(const std::map<std::string, int>& nameToPhoneNumber) {
	cout << "Current phone book (sorted by name ascending):\n";
	for (const auto& [name, phoneNumber] : nameToPhoneNumber) {
		cout << "  " << name << " -> " << phoneNumber << '\n';
	}
	cout << endl;
}

int main() {
	// std::map is an ordered associative container: keys are unique and kept sorted.
	std::map<std::string, int> nameToPhoneNumber;

	// Insertion methods
	nameToPhoneNumber["Alice"] = 5551234;              // operator[] inserts if missing, then assigns
	nameToPhoneNumber.insert({"Bob", 5552222});       // insert with initializer_list
	nameToPhoneNumber.emplace("Charlie", 5553333);    // emplace constructs in-place

	// operator[] also returns a reference; this will overwrite an existing key
	nameToPhoneNumber["Alice"] = 5550000;  // updates Alice's number

	printPhoneBook(nameToPhoneNumber);

	// Lookup
	const std::string targetName {"Bob"};
	auto it = nameToPhoneNumber.find(targetName);
	if (it != nameToPhoneNumber.end()) {
		cout << "Found " << targetName << ": " << it->second << "\n\n";
	} else {
		cout << targetName << " not found\n\n";
	}

	// count(key) returns 1 if present, 0 otherwise (since keys are unique in std::map)
	cout << "Is 'Diana' present? " << (nameToPhoneNumber.count("Diana") ? "yes" : "no") << "\n\n";

	// Erase by key
	cout << "Erasing 'Charlie'...\n";
	nameToPhoneNumber.erase("Charlie");
	printPhoneBook(nameToPhoneNumber);

	// Iterating explicitly with iterators
	cout << "Iterating with iterators:\n";
	for (auto iter = nameToPhoneNumber.begin(); iter != nameToPhoneNumber.end(); ++iter) {
		cout << "  Key: " << iter->first << ", Value: " << iter->second << '\n';
	}
	cout << endl;

	// Using a custom comparator to sort keys in descending order
	std::map<std::string, int, std::greater<std::string>> descPhoneBook;
	descPhoneBook.insert(nameToPhoneNumber.begin(), nameToPhoneNumber.end());
	descPhoneBook.emplace("Zoe", 5559999);

	cout << "Phone book with descending name order:\n";
	for (const auto& [name, phoneNumber] : descPhoneBook) {
		cout << "  " << name << " -> " << phoneNumber << '\n';
	}
	cout << endl;

	// Access with at() throws std::out_of_range if key is missing (unlike operator[])
	try {
		cout << "Alice's number (via at): " << nameToPhoneNumber.at("Alice") << "\n";
		cout << "Diana's number (via at): " << nameToPhoneNumber.at("Diana") << "\n"; // will throw
	} catch (const std::out_of_range&) {
		cout << "Tried to access missing key with at(): key not found\n";
	}

	return 0;
}

