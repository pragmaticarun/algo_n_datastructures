find_package(Threads REQUIRED)

add_executable(concepts_requires concepts_requires.cpp)
add_executable(ranges ranges.cpp)
add_executable(spaceship spaceship.cpp)
add_executable(designated_initializers designated_initializers.cpp)
add_executable(consteval_constinit_abbrev consteval_constinit_abbrev.cpp)
add_executable(span_bit_cast_source_location span_bit_cast_source_location.cpp)
add_executable(coroutines_generator coroutines_generator.cpp)
add_executable(jthread_stop_token jthread_stop_token.cpp)

if (Threads_FOUND)
  target_link_libraries(jthread_stop_token PRIVATE Threads::Threads)
endif()

