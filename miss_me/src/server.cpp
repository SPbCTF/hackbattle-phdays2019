#include <stdio.h>
#include <string.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <openssl/des.h>

#include <iostream>
#include <iomanip>
#include <string>

char flag[] = "flag{4ddr3ss_m0dif1c4t10n_15_c00l}";

int function0(char* text){
    std::cout << "This is flag: " << flag << std::endl;
    return 0;
}

int function1(char* text){
    std::cout << "You entered: " << text << std::endl;
    return 0;
}

int main(int argc, char** argv){
    int (*f)(char*) = function1;
    char string[32];
    std::string s;
    std::cout << "Hello, enter something: ";
    std::cin >> s;
    strcpy(string, s.c_str());
    f(string);
    return 0;
}