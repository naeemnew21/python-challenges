# generate permutations by recursion

def permut(a , n ,*args) :
    if n == 0 :
        yield args # generator
        return
    for i in a :
        if i not in args :
            '''yield from : to yield from recursion function '''
            yield from permut(a , n-1 , *args , i)

