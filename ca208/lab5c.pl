/*Y is the fib number of X if Y = X-1 + X-2 for all X > 1.*/

fib(1, 1).
fib(0, 1).
fib(X, Y) :-
    X1 is X - 1, X2 is X - 2, Y is X1 + X2, !.