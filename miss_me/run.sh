#!/bin/bash

socat -d -d TCP4-LISTEN:5454,fork,reuseaddr EXEC:./miss_me_server,su=nobody
