# CMake module example
add_executable(module_app main.cpp)
target_sources(module_app PRIVATE main.cpp FILE_SET CXX_MODULES FILES math.ixx)
