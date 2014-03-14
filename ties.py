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
KNOT_NAMES = ( "Corinthian"
              ,"Englebert"
              ,"Rogue"
              ,"Wayne"
              ,"Alphonse"
              ,"Fancy Hacker"
              ,"Cornwallis"
              ,"Manifesto"
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
    return Node('through', 'in')

def starter():
    return Node('left', random.choice(['in', 'out']))

def flip(value):
    # 'Flip the bit' of the provided value, providing its alternate(s)
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
        elif len(walk) > 9:
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
def get_str(knot):
    # Convert a list of nodes into a string
    str_list = [str(node) for node in knot]
    return " ".join(str_list)

def render_knot(knot):
    # Get a name from a string and return the named string
    knot_str = get_str(knot)
    if knot_str in NAMED_KNOTS:
        name = NAMED_KNOTS[knot_str]
    else:
        name = KNOT_NAMES[hash(knot_str) % len(KNOT_NAMES)]
    return "The {}: {}".format(name, knot_str)

def produce_knot(num=1):
    # Get a name from a string and return the named string
    knots = []
    for i in range(num):
        knot = render_knot(random_walk())
        if knot not in knots:
            knots.append(knot)
    return "\n".join(knots)

def named_knot(num=1):
    # Get a name from a string and return the named string
    knots = []
    while len(knots) < min(num, 25):
        knot = random_walk()
        if get_str(knot) in NAMED_KNOTS and render_knot(knot) not in knots:
            print(render_knot(knot))
            knots.append(render_knot(knot))
    return knots


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
    