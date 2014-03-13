DIRECTIONS = {'left', 'right', 'center'}
BITS = {'out', 'in'}
SHORTNAMES = {
    'left':'L',
    'right':'R',
    'center':'C',
    'out':'o',
    'in':'i'
}

def flip(value):
    if value in DIRECTIONS:
        return list(DIRECTIONS - set([value]))
    elif value in BITS:
        return (BITS - set([value])).pop()
    else:
        return value

class Node(object):

    def __init__(self, name, bit):
        self.name = name
        self.bit = bit
        self.shortname = "{}{}".format(SHORTNAMES[self.name], SHORTNAMES[self.bit])

    def __repr__(self):
        return "node {}.{}".format(self.name, self.bit)

    def __str__(self):
        return self.shortname

    def get_children(self):
        choices = flip(self.name)
        return (Node(choices[0], flip(self.bit)), Node(choices[1], flip(self.bit)))