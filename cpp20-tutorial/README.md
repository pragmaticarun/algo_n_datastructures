# C++20 Tutorial Through Examples

A compact, buildable tutorial project showcasing practical C++20 features. Each example is a small, focused program.

## Prerequisites
- A C++20-capable compiler (GCC 11+, Clang 12+, MSVC 19.30+)
- CMake 3.20+

## Build
```bash
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . -j
```

Executables will be in `build/src/`.

## Run examples
```bash
./src/concepts_requires
./src/ranges
./src/spaceship
./src/designated_initializers
./src/consteval_constinit_abbrev
./src/span_bit_cast_source_location
./src/coroutines_generator
./src/jthread_stop_token
```

## What each example shows

- Concepts and requires (`src/concepts_requires.cpp`)
  - Defines `Addable` concept with `requires` expression and return type constraint.
  - Uses constrained abbreviated function template parameters.
  - Shows `requires`-clause checking presence of `.size()`.

- Ranges pipelines (`src/ranges.cpp`)
  - Uses `std::views::iota`, `filter`, `transform`, and `take` in a composable pipeline.
  - Demonstrates lazy views and iteration.

- Three-way comparison `<=>` (spaceship) (`src/spaceship.cpp`)
  - `operator<=>` defaulted to get ordering and equality for aggregates.
  - Interoperates with associative containers like `std::set`.

- Designated initializers (`src/designated_initializers.cpp`)
  - Initializes aggregate members by name: `.x =`, `.y =` etc.

- `consteval`, `constinit`, abbreviated templates (`src/consteval_constinit_abbrev.cpp`)
  - `consteval` function must be evaluated at compile time.
  - `constinit` ensures static storage is initialized at compile time.
  - Abbreviated templates via `auto` parameters with constraints.

- `std::span`, `std::bit_cast`, `std::source_location` (`src/span_bit_cast_source_location.cpp`)
  - `std::span` for safe non-owning views.
  - `std::bit_cast` for bit-level reinterpretation (size-compatible, trivially copyable).
  - `std::source_location` to capture file/line/function.

- Coroutines generator (`src/coroutines_generator.cpp`)
  - Minimal generator type using C++20 `std::coroutine_handle` and `co_yield`.

- `std::jthread` and `std::stop_token` (`src/jthread_stop_token.cpp`)
  - Cooperative cancellation and automatic join on destruction.

## Notes
- Some libstdc++/libc++ versions require linking with threads for `std::jthread` (handled in CMake).
- If your compiler is older, update toolchain or use a newer container/image with GCC 13+ or Clang 16+.