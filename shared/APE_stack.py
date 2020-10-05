from __future__ import print_function

__author__ = 'patras'

import types

def print_stack_size(stackid, path):
    stacksize = len(path[stackid])
    print(' stack {}.{}: '.format(stackid,stacksize),end=' '*stacksize)

def print_entire_stack(stackid, path):
    if len(path[stackid]) == 0:
        print(' stack {} = []\n'.format(stackid), end='')
        return

    print(' stack {} = ['.format(stackid), end='')
    punctuation = ', '
    for i in range(0,len(path[stackid])):
        (name,args) = path[stackid][i]
        if type(name) is types.FunctionType:
            name = name.__name__
        if i >= len(path[stackid]) - 1:
            punctuation = ']\n'
        print('{}{}'.format(name, args), end=punctuation)

############################################################
# Helper functions that may be useful in domain models

def forall(seq,cond):
    """True if cond(x) holds for all x in seq, otherwise False."""
    for x in seq:
        if not cond(x): return False
    return True

def find_if(cond,seq):
    """
    Return the first x in seq such that cond(x) holds, if there is one.
    Otherwise return None.
    """
    for x in seq:
        if cond(x): return x
    return None
