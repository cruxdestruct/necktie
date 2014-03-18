# necktie

This python library is an exploration of the concepts introduced in [*The 85 Ways to Tie a Tie*][85w], by Thomas Fink & Yong Mao, and in the papers that introduced their work (available at [Dr. Fink's page on the subject][fink]).

[85w]: http://www.amazon.com/The-85-Ways-Tie-Aesthetics/dp/1841152498/
[fink]: http://www.tcm.phy.cam.ac.uk/~tmf20/tieknots.shtml

It currently is able to randomly design necktie knots, and allows the user to design necktie knots, using their system of notation. It can apply the metrics introduced in the above papers to a given knot to analyze its aesthetics. If the knot is not an established knot or one of the knots introduced in the book, it is assigned one of a number of new necktie knot names suggested by many of the members of [Hacker School](http://hackerschool.com)[^1]

[^1]: Thanks to Jay Weisskopf, Dan Wuu, Riley Shaw, Mindy Preston, Amy Hanlon, Rose Ames, Robert Lord, Zach Allaun, Andrea Fey, Lindsay Kuper, Pablo Torres, Alex Whitney, Sumana Harihareswara, Matthew Long, Will Sommers, Carl Vogel.

``` .py
>>> analyze(random_walk())

        The *Half-Windsor: Li Ro Ci Lo Ri Co Ti
        Size: 6
        Symmetry: 0
        Balance: 0
        This is a rather broad knot.
        You will not have trouble tying this knot.
        This knot will not untie when pulled out.

>>> analyze(random_walk())

        The Clove Hitch: Lo Ci Lo Ci Ro Li Co Ti
        Size: 7
        Symmetry: -2
        Balance: 2
        This is a very broad knot.
        You will not have trouble tying this knot.
        This knot will untie when pulled out.
```