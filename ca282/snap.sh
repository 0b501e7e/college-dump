#!/bin/sh

uniq -d "$@" | head -n 1
