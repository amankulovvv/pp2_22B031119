from itertools import permutations
string = input()
def perm(text):
    perms = [''.join(p) for p in permutations(text)]
    print(perms)
perm(string)