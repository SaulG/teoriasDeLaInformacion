import threading
from sys import argv

def tecnicaSaul(pattern, string):
    match = 0
    index = 0
    for s in string:
        print s, match, index
        if match == len(pattern):
            print "ENCONTRE EN ESTE INDICE: ",index
            match = 0
        if s == pattern[match]:
            match+=1
        else:
            match = 0
        index+=1
    return


def preKmp(pattern, m):
    i = 0
    kmpNext= []
    j = kmpNext[0] = -1
    while i < m:
        while j > -1 and x[i] != x[j]:
            j = kmpNext[j]
        i+=1
        j+=1
        if x[i] == x[j]:
            kmpNext[i] = kmpNext[j]
        else:
            kmpNext[i] = j
    return kmpNext

def kmp(pattern, string):
    m = len(pattern)
    n = len(string)
    #preprocesamiento
    kmpNext = preKmp(pattern, m)
    i = j = 0;
    while j < n:
        while i > -1 and pattern[i] != string[j]:
            i = kmpNext[i]
        i+=1
        j+=1
        if i >= m:
            print j - i
            i = kmpNext[i]

def preBmBc(pattern, m):
    bmBc = []
    i = 0
    while i < m - 2:
        bmBc[i] = m
        i+=1
    i = 0
    while i < m - 1:
        bmBc[pattern[i]] = m - i -1
    return bmBc

def suffixes(pattern, m):
    suff = []
    suff[m - 1] = m
    g = m - 1
    i = m - 2
    f = 0
    while i >= 0:
        if i > g and suff[i + m - 1 - f] < i - g:
            suff[i] = suff[i + m - 1 - f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pattern[g] == pattern[g + m - 1 - f]:
                g -= 1
            suff[i] = f - g
    return suff

def preBmGs(pattern, m):
    bmGs=[]
    suff = suffixes(pattern, m)
    i = m
    j = 0
    while  i >= 0:
        if suff[i] == i + 1:
            while j < m - 1 - i:
                if bmGs[j] == m:
                    bmGs[j] = m - 1 - i
                j+=1
        i-=1
    i = 0
    while i <= m - 2:
        bmGs[m - 1 - stuff[i]] = m - 1 - i
        i+=1
    return preBmGs

def boyerMoore(pattern, string):
    m = len(pattern)
    n = len(string)
    #preprocesamiento
    bmGs = preBmGs(pattern, m)
    bmBc = preBmBc(pattern, m) 
    j = 0
    while j <= n - m:
        i = m-1
        while i >= 0 and pattern[i] == string[i+j]:
            if i < 0:
                print j
                j += bmGs[0]
            else:
                if bmGs[i] > bmBc[string[i + j]] - m + 1 + i:
                    j += bmGs[i]
                else:
                    bmBc[string[i + j]] - m + 1 + i
                
def main():
    tecnicaSaul(str(argv[1]), str(argv[2]))
    boyerMoore(str(argv[1]), str(argv[2]))
    kmp(str(argv[1]), str(argv[2]))

main()
