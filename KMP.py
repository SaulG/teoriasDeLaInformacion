from sys import argv
from datetime import datetime

def KMP(text, pattern, ff):
    init_time = datetime.now()
    i = 0
    j = 0
    n = len(text)
    m = len(pattern)
    total_de_matches = list()
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            print "%s %s "%((i-j+1),(datetime.now() - init_time).microseconds/1000.00)
            total_de_matches.append(i-j+1)
            j = ff[j - 1]
        elif pattern[j] != text[i]:
            if j != 0:
                j = ff[j-1]
            else:
                i += 1
    #print "Tiempo total %s\n"%((datetime.now() - init_time).microseconds/1000.00)
    return total_de_matches

def failureFunction(P):
    j = 0
    i = 1
    f = dict()
    f[0] = 0
    m = len(P)
    while i < m:
        if P[i] == P[j]:
            f[i] = j + 1;
            i += 1
            j += 1
        elif j > 0:
            j = f[j - 1]
        else:
            f[i] = 0
            i+=1
    return f

def main():
    string = open(argv[1], 'r').read()
    text = string
    pattern = raw_input('Pattern: ')
    f = failureFunction(pattern)
    matches = KMP(text, pattern, f)
    #print matches, len(matches)
    return

main()
        
