#include <iostream>
#include <boost/asio.hpp>

int main() {
    boost::asio::io_context io;
    io.post([] {
        std::cout << "my man" << std::endl;
    });

    io.run();
    return 0;
}