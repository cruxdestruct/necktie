#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import random
from itertools import tee
from blessings import Terminal
from time import sleep
from collections import namedtuple

DIRECTIONS = {'L', 'R', 'C'}
BITS = {"o", "i"}
KNOT_NAMES = ( "Corinthian"
              ,"Rogue"
              ,"Wayne"
              ,"Alphonse"
              ,"Fancy Hacker"
              ,"Broadway"
              ,"Ace of Spades"
              ,"Flying Fox"
              ,"Tally-Ho"
              ,"Royal Hangman"
              ,"Ritchie"
              ,"Lovelace"
              ,"Dijkstra"
              ,"Russell"
              ,"Hopper"
              ,"Church"
              ,"Babbge"
              ,"Turing"
              ,"Brimley"
              ,"Subtle -Ism"
              ,"Mandalay"
              ,"Afraid"
              ,"Spaghetti"
              ,"Alphine Butterfly"
              ,"Carrick Bend"
              ,"Anchor Hitch"
              ,"Constrictor"
              ,"Clove Hitch"
              ,"Sheet Bend"
              ,"Poacher's"
              ,"Rat-tail Stopper"
              ,"Halyard Hitch"
              ,"Tubular"
              ,"Fuzzy"
              ,"DiGiorno's"
              ,"Logan's"
              ,"Knot"
              ,"Louisville Fumble"
              ,"Gordian"
              ,"Garlic"
              ,"Inferior Ascot"
              ,"Naughty Crumpet"
              ,"Flying Dutchman"
              ,"Sir Knot Appearing in This Film"
              ,"Prusik"
              ,"Trucker's"
              ,"Strange Loop"
              ,"Mark and Sweep"
              ,"Closed Cambridge"
              ,"Bent Shepherd"
              ,"Riker's Beard"
              ,"Indirect Buffer"
              ,"Auto Fill"
              ,"Right Fringe"
              ,"Meta Control"
              ,"Copy Left"
              ,"Kill and Yank"
              ,"Mark Ring"
              ,"Split Frame"
              ,"Earl Grey, Hot"
              ,"Stupid Big"
              ,"Hanging Bunny"
              ,"Wexler-Windkloppel"
              ,"Trefoil"
              ,"Garlic"
              ,"Khwarizmi"
              ,"Backus"
              ,"Boole"
              ,"Berners-Lee"
              ,"Cerf"
              ,"Engelbart"
              ,"Flowers"
              ,"Gödel"
              ,"Frege"
              ,"Wittgenstein"
              ,"Knuth"
              ,"Leibniz"
              ,"Cantor"
              ,"McCarthy"
              ,"Minsky"
              ,"von Neumann"
              ,"Thompson"
              ,"Curry"
    )
NAMED_KNOTS = {"Lo Ri Co Ti": "*Oriental"
              ,"Li Ro Li Co Ti": "*Four-in-Hand"
              ,"Lo Ri Lo Ri Co Ti": "*Kelvin"
              ,"Lo Ci Ro Li Co Ti": "*Nicky"
              ,"Lo Ci Lo Ri Co Ti": "*Pratt aka Shelby"
              ,"Li Ro Li Ro Li Co Ti": "*Victoria"
              ,"Li Ro Ci Lo Ri Co Ti": "*Half-Windsor"
              ,"Li Ro Ci Ro Li Co Ti": "*co-Half-Windsor"
              ,"Lo Ri Lo Ci Ro Li Co Ti": "*St. Andrew"
              ,"Lo Ri Lo Ci Lo Ri Co Ti": "*co-St. Andrew"
              ,"Lo Ci Ro Ci Lo Ri Co Ti": "*Plattsburgh"
              ,"Lo Ci Ro Ci Ro Li Co Ti": "*co-Plattsburgh"
              ,"Li Ro Li Co Ri Lo Ri Co Ti": "*Cavendish"
              ,"Li Co Ri Lo Ci Ro Li Co Ti": "*Windsor"
              ,"Li Co Li Ro Ci Lo Ri Co Ti": "*co-Windsor"
              ,"Li Co Ri Lo Ci Lo Ri Co Ti": "*co-Windsor 2"
              ,"Li Co Li Ro Ci Ro Li Co Ti": "*co-Windsor 3"
              ,"Lo Ri Lo Ri Co Li Ro Li Co Ti": "*Grantchester"
              ,"Lo Ri Lo Ri Co Ri Lo Ri Co Ti": "*co-Grantchester"
              ,"Lo Ri Co Li Ro Ci Lo Ri Co Ti": "*Hanover"
              ,"Lo Ri Co Ri Lo Ci Ro Li Co Ti": "*co-Hanover"
              ,"Lo Ri Co Li Ro Ci Ro Li Co Ti": "*co-Hanover 2"
              ,"Lo Ri Co Ri Lo Ci Lo Ri Co Ti": "*co-Hanover 3"
              ,"Lo Ci Ro Ci Lo Ci Ro Li Co Ti": "*Balthus"
              ,"Lo Ci Ro Ci Lo Ci Lo Ri Co Ti": "*co-Balthus"
    }

RULES_MACHINE = []


def through():
    return Node('T', 'i')

def starter():
    return Node('L', random.choice(['i', 'o']))

def flip(value):
    # 'Flip the bit' of the provided value, providing its alternate(s)
    if value in DIRECTIONS:
        return list(DIRECTIONS - set([value]))
    elif value in BITS:
        return (BITS - set([value])).pop()
    else:
        return value

def pairwise(iterable):
    #stolen from SO
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)



class Knot(object):
    """
    >>> len(Knot())
    1
    >>> len(Knot("Li Ro"))
    2
    """

    def __init__(self, value=None):
        if not value:
            self.sequence = [starter()]
        else:
            if isinstance(value, list):
                self.sequence = value
            elif isinstance(value, str):
                self.sequence = [Node(word) for word in value.split()]

    def __getitem__(self, key):
        """
        Dictionary-style access for knots.
        >>> print(Knot("Lo Ci")[-1])
        Ci
        """
        return self.sequence[key]

    def __str__(self):
        # Convert a list of nodes into a string
        return " ".join([str(node) for node in self])

    def __repr__(self):
        return " ".join([repr(node) for node in self])

    def __len__(self):
        return len(self.sequence)

    def __eq__(self, other):
        return other.__eq__(self.sequence)

    def append(self, str):
        self.sequence.append(Node(str))

    def pop(self):
        self.sequence.pop()

    def final(self):
        """
        Return name of final node.
        >>> Knot("Li").final()
        'Li'
        >>> Knot("Lo Ci Ro Li Co Ti").final()
        'Ti'
        """
        return self.sequence[-1].shortname

    def initial(self):
        return self.sequence[0].shortname

    def get_children(self):
        """
        Return possible moves of last node.
        >>> sorted(Knot("Lo Ri Co").get_children())
        ['Li', 'Ri', 'Ti']
        """
        return self[-1].get_children()
    
    def add_rule(moves):
        def decorator(func):
            RULES_MACHINE.append((func, moves))
            return func
        return decorator

    @add_rule(('Ti',))
    def finishable(self):
        """
        Whether the knot can be finished in its current state.
        >>> Knot("Lo Ri Co").finishable()
        True
        """
        return [str(node) for node in self[-3:]] in (["Ro", "Li", "Co"], ["Lo", "Ri", "Co"])

    @add_rule(('Co',))
    def two_away(self):
        """
        Whether a knot is ready to be completed with Co Ti.
        """
        return [str(node) for node in self[-2:]] in (['Ro', 'Li'], ['Lo', 'Ri'])

    @add_rule(('Li', 'Ri', 'Ro', 'Lo'))
    def leadup(self):
        """
        Whether a knot is on the 'runway', where we have to begin the finishing sequence
        """
        return not self.finishable() and (len(self) == 6 or (len(self) == 7 and self.initial() == "Lo")
                                                         or (len(self) == 5 and self.initial() == "Li"))

    @add_rule(('Ri', 'Ro', 'Li', 'Lo', 'Ci', 'Co'))
    def mid_knot(self):
        return ((1 <= len(self) < 6) and self.initial() == "Lo") or ((1 <= len(self) < 5) and self.initial() == 'Li')

    def legal_moves(self):
        """
        Get legal moves in a given position in a knot.
        >>> sorted((Knot("Lo Ri Co")).legal_moves())
        ['Ci', 'Co', 'Li', 'Lo', 'Ri', 'Ro', 'Ti']
        """
        legal_moves = set([])
        for rule_moves in RULES_MACHINE:
            if rule_moves[0](self):
                legal_moves.update(rule_moves[1])
        return legal_moves

    def legal_intersection(self):
        """
        Get intersection between legal moves and available moves of active node.
        >>> sorted(Knot("Li").legal_intersection())
        ['Co', 'Ro']
        >>> sorted(Knot("Lo Ri Co Ri Lo Ri Co").legal_intersection())
        ['Ti']
        >>> sorted(Knot("Lo Ri Co").legal_intersection())
        ['Li', 'Ri', 'Ti']
        >>> sorted(Knot("Lo").legal_intersection())
        ['Ci', 'Ri']
        """
        return list(self.get_children() & self.legal_moves())

    def one_step(self):
        """
        Add one guaranteed legal move to a knot
        """
        self.append(random.choice(self.legal_intersection()))

    def render(self):
        """
        Get a name from a string and return the named string
        """
        knot_str = str(self)
        if knot_str in NAMED_KNOTS:
            name = NAMED_KNOTS[knot_str]
        else:
            name = KNOT_NAMES[hash(knot_str) % len(KNOT_NAMES)]
        return "The {}: {}".format(name, knot_str)

    def tiable(self):
        """
        Whether a knot ends in one of the two allowed sequences.

        >>> Knot("Lo Ri Co Li Ro Li Co Ti").tiable()
        True
        >>> Knot("Li Ro Ci Lo Co Ti").tiable()
        False
        """
        return [str(node) for node in self[-4:]] in (['Ro', 'Li', 'Co', 'Ti'], ['Lo', 'Ri', 'Co', 'Ti'])

    def random_walk(self, walk=None):
        """
        Build a knot by recursive algorithm. Mutates the knot's sequence.
        """
        if not walk:
            return self.random_walk([starter()])
        elif walk[-1].shortname == 'Ti' and Knot.tiable(walk):
            self.sequence = walk
        elif walk[-1].shortname == 'Ti' and not Knot.tiable(walk):
            return self.random_walk(walk[:-4])
        elif len(walk) >= 9:
            if walk[-1].shortname == 'Co':
                if Knot.finishable(walk):
                    walk.append(Node('Ti'))
                    self.sequence = walk
                else:
                    return self.random_walk(walk[:-1])
                return self.random_walk(walk)
            else:
                return self.random_walk(walk[:-3])
        else:
            walk.append(Node(random.choice(list(walk[-1].get_children()))))
            return self.random_walk(walk)
    
    def __getattr__(self, attr):
        if attr == "analysis":
            l_r = (sum(1 for node in self.sequence if node.direction == "L"),
                  (sum(1 for node in self.sequence if node.direction == "R")))
            centers = sum(1 for node in self.sequence if node.direction == "C")
            size = len(self) - 1
            breadth = centers / size
            symmetry = l_r[1] - l_r[0]
            wise = ['-' if n[0] > n[1] else '+' for n in pairwise(self[:-1])]
            balance = sum([1 for k in pairwise(wise) if k[0] != k[1]])
            knotted = False if [str(node) for node in self[-4:]] == ["Ro", "Li", "Co", "Ti"] else True
            return Analysis(size, symmetry, balance, breadth, knotted)
        else:
            raise AttributeError
            
    def analyze(self):
        """
        Report on Fink & Mao's metrics for a given knot.
        >>> Knot("Li Co Li Ro Ci Ro Li Co Ti").analyze()
        <BLANKLINE>
                The *co-Windsor 3: Li Co Li Ro Ci Ro Li Co Ti
                Size: 8
                Symmetry: -1
                Balance: 2
                This is a rather broad knot.
                This knot will untie when pulled out.
        <BLANKLINE>
        """
        analysis = self.analysis
        breadth = analysis.breadth

        if breadth < .25:
            shape = "very narrow"
        elif .25 <= breadth < (1/3):
            shape = "rather narrow"
        elif (1/3) <= breadth < .4:
            shape = "rather broad"
        elif .4 <= breadth:
            shape = 'very broad'

        print("""
        {render}
        Size: {size}
        Symmetry: {symmetry}
        Balance: {balance}
        This is a {shape} knot.
        This knot {knotted} untie when pulled out.
            """.format(render=self.render(),size=analysis.size, shape=shape, 
                       symmetry=analysis.symmetry, balance=analysis.balance, 
                       knotted=('will not' if analysis.knotted else 'will')))

Analysis = namedtuple('Analysis', ['size', 'symmetry', 'balance','breadth', 'knotted'])
        
class Node(object):
    """
    We implement a tie as a series of nodes. Each node is a sort of state machine
    which can return its valid children depending on its current state.
    """
    def __init__(self, *args):
        try:
            direction, bit = args
            self.direction = direction
            self.bit = bit
            self.shortname = "{}{}".format(self.direction, self.bit)
        except ValueError:
            self.shortname = args[0].title()
            self.direction = self.shortname[0]
            self.bit = self.shortname[1]
        if not (self.shortname and self.bit and self.direction):
            raise AttributeError('Bad node created.')

    def __repr__(self):
        return "node {}.{}".format(self.direction, self.bit)

    def __str__(self):
        return self.shortname

    def __eq__(self, other):
        return other.__eq__(self.shortname)

    def __gt__(self, other):
        return (self.direction == "L" and other.direction == "R") or (self.direction == "R" and other.direction == "C") or (self.direction == "C" and other.direction == "L")

    def get_children(self):
        choices = flip(self.direction)
        children = set([choices[0]+flip(self.bit), choices[1]+flip(self.bit)])
        if self.shortname == "Co":
            children.add('Ti')
        elif self.shortname == "Ti":
            children = set([])
        return children

def linear_build():
    """
    A knot generating algorithm that never makes a wrong move.
    """
    k = Knot()
    while True:
        # print('*' * 10)
        # print("knot is", str(knot))
        # print("children are", knot.get_children())
        # print("legal moves are", legal_moves(knot))
        # print("Intersection is", knot.get_children() & legal_moves(knot))
        k.one_step()
        if k.final() == "Ti":
            return k
            
def produce(num=1):
    """
    Generate n random unique knots
    """
    knots = set([])
    while len(knots) < num:
        knots.add(str(linear_build()))
    return "\n".join(sorted(list(knots)))

def named(num=1):
    """
    Produce n unique named knots
    """
    knots = set([])
    while len(knots) < min(num, 25):
        knot = str(linear_build())
        if knot in NAMED_KNOTS and knot not in knots:
            print(Knot(knot).render())
            knots.add(str(knot))

 
def tie_a_tie():
    """
    Interactive tie tying.
    """
    def throw():
        print(term.clear())
        with term.location(10, term.height):
            print("Please enter a valid choice.")
            sleep(1)
            print(term.clear())
    def start_knot():
        print(term.clear())
        starting_point = input("Start in or out? ").lower()
        if starting_point in ["i", "in"]:
            return Knot('Li')
        elif starting_point in ["o", "out"]:
            return Knot('Lo')
        else:
            return Knot()

    term = Terminal()
    with term.location(0,0):
        tie = start_knot()
        while tie.final() != 'Ti':
            print(term.clear())
            choices = tie.legal_intersection()
            tie_str = str(tie)
            try:
                while True:
                    with term.location(0,3):
                        possibilities = [name for walk, name in NAMED_KNOTS.items() if tie_str == walk[:len(tie_str)]]
                        print("\nPossible knots:\n{}\n".format("\n".join(possibilities)))
                    next_step = input("Your knot so far: {}\nNext step ({}{}): "
                               .format(tie_str, choices, " back" if len(tie) > 1 else "")).title()
                    if next_step == "Back" and len(tie) > 1:
                        tie.pop()
                        break
                    if next_step == "Back" and len(tie) == 1:
                        tie = start_knot()
                        break
                    if next_step in choices:
                        tie.append(next_step)
                        break
                    if not next_step:
                        tie.append(choices[0])
                        break
                    else: 
                        throw()   
            except:
                throw()                 
        print(term.clear())
    tie.analyze()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(produce(85))
    # tie_a_tie()
    # import cProfile
    # cProfile.run('produce(85)')
    # print(produce(85))