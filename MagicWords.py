# TopCoder SRM 433 R1D1L1
__author__ = 'kedar'

def permutations(n: int):
    if n < 1:
        return []
    elif n == 1:
        return [[0]]
    perms = []
    for p in permutations(n-1):
        for x in range(len(p) + 1):
            perm=list(p)
            perm.insert(x, n-1)
            perms.append(perm)
    return perms

def shift(word:str, i:int):
    return word[i:] + word[:i]

def shiftK(word: str):
    counter=0
    for i in range(len(word)):
        if shift(word, i) == word:
            counter+=1
    return counter

def count (S: list, K: int):
    if len(''.join(S)) % K != 0: # if the length of the string isn't divisible by a K, it can't have magic words
        return 0

    counter = 0
    for perm in permutations(len(S)): # perm is a list
        word = ''.join(S[n] for n in perm) # make word from perm
        if shiftK(word) == K:
            counter += 1
    return counter




