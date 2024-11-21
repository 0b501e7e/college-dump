myElem(X, [X | _]).

myElem(X, [_ | T]) :-
    myElem(X, T).


myHead(X, [X| _]).

myLast(X, [X]).
myLast(X, [_|T]) :- myLast(X, T).

myTail(X, [_|X]).

myAppend([], L, L).
myAppend([X|L1], L2, [X|L3]) :-
    myAppend(L1, L2, L3).

myReverse([], []).
myReverse([X|T], Y) :-
    myReverse(T, T1), myAppend(T1, [X], Y).

myDelete(X, [X|T], T).
myDelete(X, [Y|T], [Y|T1]) :- 
    myDelete(X, T, T1).
