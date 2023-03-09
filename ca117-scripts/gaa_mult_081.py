#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def goals_to_points(self):
        return self.goals * 3 + self.points

    def __str__(self):
        return f"{self.goals} goal(s) and {self.points} point(s)"

    def __eq__(self, other):
        return self.goals_to_points() == other.goals_to_points()

    def __gt__(self, other):
        return self.goals_to_points() > other.goals_to_points()

    def __lt__(self, other):
        return self.goals_to_points() < other.goals_to_points()

    def __ge__(self, other):
        return self.goals_to_points() >= other.goals_to_points()

    def __le__(self, other):
        return self.goals_to_points() <= other.goals_to_points()

    def __add__(self, other):
        tg = self.goals + other.goals
        tp = self.points + other.points
        return Score(tg, tp)

    def __sub__(self, other):
        newg = self.goals - other.goals
        newp = self.points - other.points
        return Score(newg, newp)

    def __iadd__(self, other):
        q = self + other
        self.goals, self.points = q.goals, q.points
        return self

    def __isub__(self, other):
        z = self - other
        self.goals, self.points = z.goals, z.points
        return self

    def __mul__(self, other):
        mulg = self.goals * other
        mulp = self.points * other
        return Score(mulg, mulp)

    def __imul__(self, other):
        i = self * other
        self.goals, self.points = i.goals, i.points
        return self

    def __rmul__(self, other):
        rmulg = self.goals * other
        rmulp = self.points * other
        return Score(rmulg, rmulp)


def points_to_goals(p):
    gls, pts = divmod(p, 3)
    return Score(gls, pts)


def main():

    # Create some instances of Score
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(2, 11)
    s5 = Score(1, 1)

    # Display
    print('Display...')
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # Multiplication
    print('Multiplication...')
    s2 = s2 * 2
    print(s2)
    print(s2 > s3)

    # Right multiplication
    print('Right multiplication...')
    s2 = 2 * s2
    print(s2)
    print(s2 > s3)

    # In-place multiplication
    print('In-place multiplication...')
    s2alias = s2
    s2 *= 2
    print(s2)
    print(s2alias)
    print(s2 == s2alias)


if __name__ == '__main__':
    main()
