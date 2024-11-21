north(a, f).
north(a, k).
north(a, p).
north(b, g).
north(b, l).
north(b, w).
north(c, h).
north(c, z).
north(c, r).
north(d, i).
north(d, n).
north(d, u).
north(e, j).
north(e, o).
north(e, t).
north(f, k).
north(f, p).
north(k, p).
north(g, l).
north(g, w).
north(l, w).
north(h, z).
north(h, r).
north(z, r).
north(i, n).
north(i, u).
north(n, u).
north(j, o).
north(j, t).
north(o, t).

west(a, b).
west(a, c).
west(a, d).
west(a, e).
west(f, g).
west(f, h).
west(f, i).
west(f, j).
west(k, l).
west(k, z).
west(k, n).
west(k, o).
west(p, w).
west(p, r).
west(p, u).
west(p, t).
west(b, c).
west(b, d).
west(b, e).
west(c, d).
west(c, e).
west(g, h).
west(g, i).
west(g, j).
west(h, i).
west(h, j).
west(i, j).
west(l, z).
west(l, n).
west(l, o).
west(z, n).
west(z, o).
west(n, o).
west(w, r).
west(w, u).
west(w, t).
west(r, u).
west(r, t).
west(u, t).



south(p, k).
south(p, f).
south(p, a).
south(w, l).
south(w, g).
south(w, b).
south(r, z).
south(r, h).
south(r, c).
south(u, n).
south(u, i).
south(u, d).
south(t, o).
south(t, j).
south(t, e).

east(e, d).
east(e, c).
east(e, b).
east(e, a).
east(j, i).
east(j, h).
east(j, g).
east(j, f).
east(o, n).
east(o, w).
east(o, l).
east(o, k).
east(t, u).
east(t, r).
east(t, z).
east(t, p).




duenorth(X, Y) :- north(X, Y).
duesouth(X, Y) :- duenorth(Y, X).
dueeast(X, Y) :- duewest(Y, X).
duewest(X, Y) :- west(X, Y).
duenorthwest(X, Y) :- west(X, Z), duenorth(Z, Y).
duenortheast(X, Y) :- dueeast(X, Z), duenorth(Z, Y).
duesouthwest(X, Y) :- west(X, Z), duesouth(Z, Y).
duesoutheast(X, Y) :- dueeast(X, Z), duesouth(Z, Y).
