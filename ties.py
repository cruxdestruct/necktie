import random

DIRECTIONS = {'left', 'right', 'center'}
BITS = {'out', 'in'}
SHORTNAMES = {
    'left'   :'L',
    'right'  :'R',
    'center' :'C',
    'out'    :'o',
    'in'     :'i',
    'through':'T'
}
KNOT_NAMES = ( "The Corinthian"
              ,"The Englebert"
              ,"The Rogue"
              ,"The Wayne"
              ,"The Alphonse"
              ,"The Fancy Hacker"
              ,"The Cornwallis"
              ,"The Manifesto"
              ,"The Broadway"
              ,"The Ace of Spades"
              ,"The Flying Fox"
              ,"The Tally-Ho"
              ,"The Royal Hangman"
              ,"The Ritchie"
              ,"The Lovelace"
              ,"The Dijkstra"
              ,"The Russell"
              ,"The Hopper"
              ,"The Church"
              ,"The Babbge"
              ,"The Turing"
              ,"The Brimley"
              ,"The Subtle -Ism"

    )
NAMED_KNOTS = { "Lo Ri Co Ti": "*The Oriental"
              ,"Li Ro Li Co Ti": "*The Four-in-Hand"
              ,"Lo Ri Lo Ri Co T": "*The Kelvin"
              ," Lo Ci Ro Li Co T": "*The Nicky"
              ,"Lo Ci Lo Ri Co T": "*The Pratt aka The Shelby"
              ,"Li Ro Li Ro Li Co T": "*The Victoria"
              ,"Li Ro Ci Lo Ri Co T": "*The Half-Windsor"
              ,"Li Ro Ci Ro Li Co T": "*The co-Half-Windsor"
              ,"Lo Ri Lo Ci Ro Li Co T": "*The St. Andrew"
              ,"Lo Ri Lo Ci Lo Ri Co T": "*The co-St. Andrew"
              ,"Lo Ci Ro Ci Lo Ri Co T": "*The Plattsburgh"
              ,"Lo Ci Ro Ci Ro Li Co T": "*The co-Plattsburgh"
              ,"Li Ro Li Co Ri Lo Ri Co T": "*The Cavendish"
              ,"Li Co Ri Lo Ci Ro Li Co T": "*The Windsor"
              ,"Li Co Li Ro Ci Lo Ri Co T ": "*The co-Windsor"
              ,"Li Co Ri Lo Ci Lo Ri Co T": "*The co-Winsdor 2"
              ,"Li Co Li Ro Ci Ro Li Co T": "*The co-Windsor 3"
              ,"Lo Ri Lo Ri Co Li Ro Li Co T": "*The Grantchester"
              ,"Lo Ri Lo Ri Co Ri Lo Ri Co T": "*The co-Grantchester"
              ,"Lo Ri Co Li Ro Ci Lo Ri Co T": "*The Hanover"
              ,"Lo Ri Co Ri Lo Ci Ro Li Co T": "*The co-Hanover"
              ,"Lo Ri Co Li Ro Ci Ro Li Co T": "*The co-Hanover 2"
              ,"Lo Ri Co Ri Lo Ci Lo Ri Co T": "*The co-Hanover 3"
              ,"Lo Ci Ro Ci Lo Ci Ro Li Co T": "*The Balthus"
              ,"Lo Ci Ro Ci Lo Ci Lo Ri Co T": "*The co-Balthus"
    }
def through():
    return Node('through', 'in')

def starter():
    return Node('left', random.choice(['in', 'out']))

def flip(value):
    if value in DIRECTIONS:
        return list(DIRECTIONS - set([value]))
    elif value in BITS:
        return (BITS - set([value])).pop()
    else:
        return value

def random_walk(walk=[]):
        if not walk:
            return random_walk([starter()])
        elif walk[-1] == Node('Ti'):
            return walk
        elif len(walk) > 10:
            walk.pop()
            while walk and walk[-1] != Node('Co'):
                walk.pop()
            if not walk:
                walk = random_walk(walk)
            else:
                walk.append(through())
            return walk 
        else:
            walk.append(random.choice(walk[-1].get_children()))
            return random_walk(walk)

def render_knot(list):
    str_list = [str(node) for node in list]
    knot_str = " ".join(str_list)
    if knot_str in NAMED_KNOTS:
        name = NAMED_KNOTS[knot_str]
    else:
        name = KNOT_NAMES[hash(knot_str) % len(KNOT_NAMES)]
    return "{}: {}".format(name, knot_str)

def produce_knot(num=1):
    knots = []
    for i in range(num):
        knot = render_knot(random_walk())
        if knot not in knots:
            knots.append(knot)
    return "\n".join(knots)


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

    def __repr__(self):
        return "node {}.{}".format(self.name, self.bit)

    def __str__(self):
        return self.shortname

    def __eq__(self, other):
        return self.shortname == other.shortname

    def get_children(self):
        choices = flip(self.name)
        children = [Node(choices[0], flip(self.bit)), Node(choices[1], flip(self.bit))]
        if self == Node("Co"):
            children.append(Node('through','in'))
        return children

if __name__ == "__main__":
    print(produce_knot(25))

