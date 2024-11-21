CA282 Addition repo
-------------------

src/         - various implementations of a program to add together
               their command-line arguments.

src/Makefile - contains a target "build" which should build any
               executables (for languages like C or Java).

Makefile     - contains a target "test" which "tests" the various
               implementations.  Poor man's tests, but you should
	       be able to work out what's going on.

Example:

    zsh src/add-arguments.zsh 1 -2 3
    # Writes "6" to standard output.

Report on your progress
----------------------

Had to remove "-x" flag from grep.
