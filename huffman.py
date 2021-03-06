from sys import argv

class Node:
    def __init__(self, symbol, nodeLeft, nodeRight, frequency):
        self.label = ''
        self.symbol = symbol
        self.nodeLeft = nodeLeft
        self.nodeRight = nodeRight
        self.frequency = frequency
        return

    def __repr__(self):
        return '( %s ) [%s] %d' % (self.label, str(self.symbol), self.frequency)

    def name(self, prefix):
        self.label = prefix
        if self.nodeLeft is not None:
            self.nodeLeft.name('%s1' % self.label)
        if self.nodeRight is not None:
            self.nodeRight.name('%s0' % self.label)
        return

    def decode(self, binary):
        if self.symbol is not None:
            return (self.symbol, binary)
        else:
            assert(self.nodeLeft is not None)
            assert(self.nodeRight is not None)
            bit = binary[0]
            binary = binary[1:]
            if bit == '1':
                return self.nodeLeft.decode(binary)
            elif bit == '0':
                return self.nodeRight.decode(binary)
            else:
                print 'o_O'
        return

    def insert(self, dictionary):
        if self.nodeLeft is not None:
            self.nodeLeft.insert(dictionary)
        if self.nodeRight is not None:
            self.nodeRight.insert(dictionary)
        if self.symbol is not None:
            dictionary[self.symbol] = self.label
        return

def main():
    print argv[1]
    archivo =  open(argv[1], 'r')
    datos = ''
    for line in archivo:
        datos = '%s%s'%(datos, line)
    dictionary = dict()
    for s in datos:
        if s in dictionary.keys():
            dictionary[s] += 1
        else:
            dictionary[s] = 1
    
    node_list = list()
    for d in dictionary.keys():
        node_list.append(Node(d, None, None, dictionary[d] ))

    while len(node_list) > 1:
        node_list.sort(key=lambda n: n.frequency)
        min1 = node_list.pop(0)
        min2 = node_list.pop(0)
        node_list.append(Node(None, min1, min2, min1.frequency + min2.frequency)) 

    root = node_list.pop(0)
    root.name('')
    code = dict()
    root.insert(code)

    binary = ''
    for s in datos:
        binary = '%s%s' % (binary, code[s])
    copy = binary
            
    recovered = '' 
    while len(binary) > 0:
        (symbol, binary) = root.decode(binary)
        recovered = '%s%s' % (recovered, symbol)
    print recovered

    decoder = dict()
    for symbol in code:
        decoder[code[symbol]] = symbol

    print decoder
    print copy
    
    alternative = ''
    while len(copy) > 0:
        word = ''
        while word not in decoder:
            bit = copy[0]
            copy = copy[1:]
            word = '%s%s' % (word, bit)
        alternative = '%s%s' % (alternative, decoder[word])
    print alternative
        

main()
