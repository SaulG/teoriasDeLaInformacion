from sys import argv
from datetime import datetime
def matching(word, match):
    contador = 0
    init_time = datetime.now()
    y = 0
    while (y < len(word)):
        for x in xrange(len(match)):
            #print "Word: ",word[y]," Match: ",match[x]
            print match[x], word[y+x]
            if word[y+x] == match[x]:
                matching = True
                contador+=1
                if contador == len(match):
                    print "%s %s"%((y-len(match)),(datetime.now() - init_time).microseconds/1000.00)
                    y+=len(match)
            else:
                contador = 0
                matching = False
            if not matching:
                break
        y +=1
    print "Tiempo total %s\n"%((datetime.now() - init_time).microseconds/1000.00)
def main():
    word = open(argv[1], 'r').read()
    match = raw_input("Pattern: ")
    matching(word, match)
main()
