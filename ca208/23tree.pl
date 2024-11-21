bt(L, X, R).
threenode(L, R1, M, R2, R).


member(X, bt(_, X, _)).

member(X, bt(L, Y, _)) :-
    X =< Y, member(X, L).

member(X, bt(_, _, R)) :-
    member(X, R).

member(X, threenode(_, X, _, _, _)).
member(X, threenode(_, R1, _, X, _)) :-
    X > R1.


member(X, threenode(L, R1, _, _, _,)) :-
    X =< R1, member(X, L).

member(X, threenode(_, R1, Y, R2, _)) :-
    X > R1, X =< R2, member(X, Y).

member(X, threenode(_,  _, _, R2, Y)) :-
    X > R2, member(X, Y).

addnode(nil, X, Y, threenode(nil, X, nil, Y, nil)) :- 
    X =< Y.

addnode(threenode(L, R1, M, R2, R), X, threenode(L1, R1, M, R2, R)) :-
    X =< R1, addnode(L, X, L1).

addnode(threenode(L, R1, M, R2, R), X, threenode(L, R1, M1, R2, R)) :-
    X > R1, X =< R2, addnode(M, X, M1).

addnode(threenode(L, R1, M, R2, R), X, threenode(L, R1, M, R2, RR)) :-
    X > R2, addnode(R, X, RR).


addnode(nil, X, bt(nil, X, nil)).

addnode(bt(L, Y, R), X, bt(L1, Y, R)) :-
    X =< Y, addnode(L, X, L1).

addnode(bt(L, Y, R), X, bt(L, Y, R1)) :-
    addnode(R, X, R1).

add(X, T1, T2) :- 
    addnode(T1, X, T2).

height(null, 0).

height(bt(L, _, R), H) :-
    height(L, H1), height(R, H2), H is max(H1, H2) + 1.
