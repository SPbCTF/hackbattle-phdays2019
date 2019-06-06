
CC=gcc

.PHONY: all clean

all: miss_me

clean:
	rm `ls | grep -vE '(.cpp\$$|Makefile)'` 2> /dev/null

miss_me: miss_me.cpp server.cpp
	g++ miss_me.cpp -o miss_me -no-pie -fno-stack-protector
	g++ server.cpp -o miss_me_server -no-pie -fno-stack-protector