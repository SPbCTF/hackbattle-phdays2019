#!/bin/bash

socat -d -d TCP4-LISTEN:7777,fork,reuseaddr EXEC:./server,su=nobody
