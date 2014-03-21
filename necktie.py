#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import random
from itertools import tee
from blessings import Terminal
from time import sleep

DIRECTIONS = {'L', 'R', 'C'}
BITS = {"o", "i"}
SHORTNAMES = {
    'L'   :'L',
    "R"  :'R',
    "C" :'C',
    "o"    :'o',
    "i"     :'i',
    "T":'T'
}
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
NAMED_KNOTS = {"Lo Ri Co Ti": "*Oriental"#
              ,"Li Ro Li Co Ti": "*Four-in-Hand"#
              ,"Lo Ri Lo Ri Co Ti": "*Kelvin"#
              ,"Lo Ci Ro Li Co Ti": "*Nicky"
              ,"Lo Ci Lo Ri Co Ti": "*Pratt aka Shelby"#
              ,"Li Ro Li Ro Li Co Ti": "*Victoria"#
              ,"Li Ro Ci Lo Ri Co Ti": "*Half-Windsor"#
              ,"Li Ro Ci Ro Li Co Ti": "*co-Half-Windsor"#
              ,"Lo Ri Lo Ci Ro Li Co Ti": "*St. Andrew"#
              ,"Lo Ri Lo Ci Lo Ri Co Ti": "*co-St. Andrew"#
              ,"Lo Ci Ro Ci Lo Ri Co Ti": "*Plattsburgh"#
              ,"Lo Ci Ro Ci Ro Li Co Ti": "*co-Plattsburgh"#
              ,"Li Ro Li Co Ri Lo Ri Co Ti": "*Cavendish"#
              ,"Li Co Ri Lo Ci Ro Li Co Ti": "*Windsor"#
              ,"Li Co Li Ro Ci Lo Ri Co Ti": "*co-Windsor"
              ,"Li Co Ri Lo Ci Lo Ri Co Ti": "*co-Windsor 2"#
              ,"Li Co Li Ro Ci Ro Li Co Ti": "*co-Windsor 3"#
              ,"Lo Ri Lo Ri Co Li Ro Li Co Ti": "*Grantchester"#
              ,"Lo Ri Lo Ri Co Ri Lo Ri Co Ti": "*co-Grantchester"#
              ,"Lo Ri Co Li Ro Ci Lo Ri Co Ti": "*Hanover"#
              ,"Lo Ri Co Ri Lo Ci Ro Li Co Ti": "*co-Hanover"#
              ,"Lo Ri Co Li Ro Ci Ro Li Co Ti": "*co-Hanover 2"#
              ,"Lo Ri Co Ri Lo Ci Lo Ri Co Ti": "*co-Hanover 3"#
              ,"Lo Ci Ro Ci Lo Ci Ro Li Co Ti": "*Balthus"#
              ,"Lo Ci Ro Ci Lo Ci Lo Ri Co Ti": "*co-Balthus"#
    }
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

def finishable(knot):
    return knot[-3:] in (from_str("Ro Li Co"), from_str("Lo Ri Co"))

def penultimate(knot):
    return len(knot) == 8 and knot[0].shortname == "Lo" or len(knot) == 7 and knot[0].shortname == 'Li'

def antepenultimate(knot):
    return len(knot) == 7 and knot[0].shortname == "Lo" or len(knot) == 6 and knot[0].shortname == 'Li'

def preantepenultimate(knot):
    return len(knot) == 6 and knot[0].shortname == "Lo" or len(knot) == 5 and knot[0].shortname == 'Li'

def mid_knot(knot):
    return ((1 <= len(knot) < 6) and knot[0].shortname == "Lo") or ((1 <= len(knot) < 5) and knot[0].shortname == 'Li')

def legal_moves(knot):
    """
    Get legal moves in a given position in a knot.
    >>> legal_moves(from_str("Li"))
    {'Ro', 'Ri', 'Lo', 'Li', 'Co', 'Ci'}
    """
    legal_moves = set([])
    # import pdb
    # pdb.set_trace()
    if penultimate(knot):
        legal_moves.update(['Co'])
    elif antepenultimate(knot):
        legal_moves.update(['Li', 'Ri'])
    elif preantepenultimate(knot):
        legal_moves.update(['Ro', 'Lo'])
    elif mid_knot(knot):
        legal_moves.update(['Ri', 'Ro', 'Li', 'Lo', 'Ci', 'Co'])
    if finishable(knot):
        legal_moves.update(['Ti'])
    return legal_moves

def linear_build():
    # TODO : this only produces 69 knots.
    knot = [starter()]
    while True:
        # print("knot is", get_str(knot))
        # print("children are", knot[-1].get_children())
        # print("legal moves are", legal_moves(knot))
        # print("Intersection is", knot[-1].get_children() & legal_moves(knot))
        knot.extend(from_str(random.choice(list(knot[-1].get_children() & legal_moves(knot)))))
        if knot[-1].shortname == "Ti":
            return knot
    
def from_str(str):
    words = str.split()
    return [Node(word) for word in words]

def get_str(knot):
    # Convert a list of nodes into a string
    str_list = [str(node) for node in knot]
    return " ".join(str_list)

def render(knot):
    # Get a name from a string and return the named string
    knot_str = get_str(knot)
    if knot_str in NAMED_KNOTS:
        name = NAMED_KNOTS[knot_str]
    else:
        name = KNOT_NAMES[hash(knot_str) % len(KNOT_NAMES)]
    return "The {}: {}".format(name, knot_str)

def tiable(knot):
    return knot[-4:] in (from_str("Ro Li Co Ti"), from_str("Lo Ri Co Ti"))

def random_walk(walk=[]):
        # print ("walk is ", get_str(walk))
        if not walk:
            return random_walk([starter()])
        elif walk[-1].shortname == 'Ti' and tiable(walk):
            return walk
        elif walk[-1].shortname == 'Ti' and not tiable(walk):
            return random_walk(walk[:-4])
        elif len(walk) >= 9:
            if walk[-1].shortname == 'Co':
                if finishable(walk):
                    walk.append(Node('Ti'))
                    return walk
                else:
                    return random_walk(walk[:-1])
            # if walk[-1].shortname == 'Co':
            #     walk.append(Node('Ti'))
                return random_walk(walk)
            else:
                return random_walk(walk[:-3])
        else:
            walk.append(random.choice(walk[-1].get_children()))
            return random_walk(walk)
            
def produce(num=1):
    # Generate n random unique knots
    knots = set([])
    while len(knots) < num:
        knots.add(get_str(random_walk()))
    return "\n".join(sorted(list(knots)))

def named(num=1):
    # Produce n unique named knots
    knots = set([])
    while len(knots) < min(num, 25):
        knot = get_str(random_walk())
        if knot in NAMED_KNOTS and knot not in knots:
            print(knot)
            knots.add(get_str(knot))
    return knots

def analyze(knot):
    """
    Report on Fink & Mao's metrics for a given knot.
    >>> analyze(from_str("Li Co Li Ro Ci Ro Li Co Ti"))
    <BLANKLINE>
            The *co-Windsor 3: Li Co Li Ro Ci Ro Li Co Ti
            Size: 8
            Symmetry: -1
            Balance: 2
            This is a rather broad knot.
            This knot will untie when pulled out.
    <BLANKLINE>
    """
    l_r = (sum(1 for node in knot if node.name == "L"),
              (sum(1 for node in knot if node.name == "R")))
    centers = sum(1 for node in knot if node.name == "C")
    size = len(knot) - 1
    breadth = centers / size
    symmetry = l_r[1] - l_r[0]
    wise = ['-' if n[0] > n[1] else '+' for n in pairwise(knot[:-1])]
    balance = sum([1 for k in pairwise(wise) if k[0] != k[1]])
    knotted = True
    if breadth < .25:
        shape = "very narrow"
    elif .25 <= breadth < .33:
        shape = "rather narrow"
    elif .33 <= breadth < .4:
        shape = "rather broad"
    elif .4 <= breadth:
        shape = 'very broad'
    if knot[-4:] == from_str("Ro Li Co Ti"):
        knotted = False
    
    print("""
        {render}
        Size: {size}
        Symmetry: {symmetry}
        Balance: {balance}
        This is a {shape} knot.
        This knot {knotted} untie when pulled out.
        """.format(render=render(knot),size=size, shape=shape, symmetry=symmetry, balance=balance, knotted=('will not' if knotted else 'will')))
  
def tie_a_tie():
    # Interactive tie tying.
    term = Terminal()
    with term.location(0,0):
        print(term.clear())
        starting_point = input("Start in or out? ").lower()
        if starting_point in ["i", "i"]:
            tie = [Node('Li')]
        elif starting_point in ["o", "o"]:
            tie = [Node('Lo')]
        else:
            tie = [starter()]
        while tie[-1] != Node('Ti'):
            print(term.clear())
            choices = get_str(tie[-1].get_children())
            tie_str = get_str(tie)
            while True:
                with term.location(0,3):
                    possibilities = []
                    for name in NAMED_KNOTS.keys():
                        if tie_str == name[:len(tie_str)]:
                            possibilities.append(NAMED_KNOTS[name])
                    print("\nPossible knots:\n{}\n".format("\n".join(possibilities)))
                next = input("Your knot so far: {}\nNext step ({}{}): ".format(tie_str, choices, 
                                                                        " back" if len(tie) > 1 else ""))
                if next == "back":
                    tie.pop()
                    break
                else:
                    try:
                        if next in choices:
                            tie.append(Node(next))
                            break
                        else: 
                            print(term.clear())
                            with term.location(10, term.height):
                                print("Please enter a valid choice.")
                                sleep(1)
                                print(term.clear())
                                pass
                    except:
                        print(term.clear())
                        with term.location(10, term.height):
                            print("Please enter a valid choice.")
                            sleep(1)
                            print(term.clear())
                            pass
        print(term.clear())
    analyze(tie)


class Node(object):
    """
    We implement a tie as a series of nodes. Each node is a sort of state machine
    which can return its valid children depending on its current state.
    """
    def __init__(self, *args):
        try:
            name, bit = args
            self.name = name
            self.bit = bit
            self.shortname = "{}{}".format(SHORTNAMES[self.name], SHORTNAMES[self.bit])
        except ValueError:
            self.shortname = args[0]
            for key, value in SHORTNAMES.items():
                if self.shortname[0] == value:
                    self.name = key
                if self.shortname[1] == value:
                    self.bit = key
        if not (self.shortname and self.bit and self.name):
            raise AttributeError('Bad node created.')

    def __repr__(self):
        return "node {}.{}".format(self.name, self.bit)

    def __str__(self):
        return self.shortname

    def __eq__(self, other):
        return self.shortname == other.shortname

    def __gt__(self, other):
        return (self.name == "L" and other.name == "R") or (self.name == "R" and other.name == "C") or (self.name == "C" and other.name == "L")

    def get_children(self):
        choices = flip(self.name)
        children = set([choices[0]+flip(self.bit), choices[1]+flip(self.bit)])
        if self.shortname == "Co":
            children.add('Ti')
        elif self.shortname == "Ti":
            children = set([])
        return children

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(produce(85))
    # tie_a_tie()
    # import cProfile
    # cProfile.run('produce(85)')
    # print(produce(85))