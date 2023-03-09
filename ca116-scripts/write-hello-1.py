#!/usr/bin/env python3

message = "Hello world."

fname = "hello.txt"

with open(fname, "w") as f:
  f.write(message + "\n")
