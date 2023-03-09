#!/bin/sh

while read var
do
test ! -f "$var" && echo "$var" && exit
done
