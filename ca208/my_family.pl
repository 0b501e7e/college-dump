/* FACTS */

parents(david, george, noreen).
parents(jennifer, george, noreen).
parents(georgejr, george, noreen).
parents(scott, george, noreen).
parents(joanne, george, noreen).
parents(jessica, david, edel).
parents(clara, david, edel).
parents(michael, david, edel).
parents(laura, georgejr, susan).
parents(anna, scott, siobhan).


/* Relationships */

father(X, Y) :- parents(Y, X, _).
male(X) :- father(X, _).

mother(X, Y) :- parents(Y, _, X).
female(X) :- mother(X, _).

grandfather(X, Y) :- father(X, Z), father(Z, Y).
grandfather(X, Y) :- father(X, Z), mother(Z, Y).

grandmother(X, Y) :- mother(X, Z), mother(Z, Y).
grandmother(X, Y) :- mother(X, Z), father(Z, Y).

brother(X, Y) :- male(X), father(Z, X), father(Z, Y).

sibling(X, Y) :- parents(X, I, J), parents(Y, I, J).

sister(X, Y) :- female(X), father(Z, X), father(Z, Y).

uncle(X, Y) :- male(X), parents(Y, Z, _), brother(Z, X).
aunt(X, Y) :- female(X), parents(Y, Z, _), sister(Z, X).
cousin(X, Y) :- parents(X, Z, _), parents(Y, K, _), sibling(Z, K).
