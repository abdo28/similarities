#for sentences -_-
from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    alist = a.splitlines()
    blist = b.splitlines()

    common = set()
    commons = []
    for als in alist:
        for bls in blist:
            if als == bls:
                common.add(als)

    for com in common:
        commons.append(com)
    return commons


def sentences(a, b):
    """Return sentences in both a and b"""

    alist = sent_tokenize(a, language='english')
    blist = sent_tokenize(b, language='english')

    common = set()
    commons = []
    for als in alist:
        for bls in blist:
            if als == bls:
                common.add(als)

    for com in common:
        commons.append(com)
    return commons



def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    alist = []
    blist = []

    for ass in range(0,(len(a)+1)-n,1):
        alist.append(a[ass:(ass+n)])

    for bss in range(0,(len(b)+1)-n,1):
        blist.append(b[bss:(bss+n)])

    common = set()
    commons = []
    for als in alist:
        for bls in blist:
            if als == bls:
                common.add(als)

    for com in common:
        commons.append(com)
    return commons