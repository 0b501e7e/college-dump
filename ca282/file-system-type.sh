#!/bin/sh

for var in "$@"
do
if test -f  "$var"
then
echo "$var file"
elif test -d "$var"
then
echo "$var directory"
else
echo "$var does not exist"
fi
done
