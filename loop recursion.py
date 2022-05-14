'''
    for i in a :
         for j in a :
               for k in a :
                      ..... n of loop ...
                      return i,j,k,...,n
NOTE :
           maximum of n = 995
'''
def permut(a , n , *args) :
    if n == 0 :
        yield args
        return
    for i in a :
        yield from permut(a , n-1 , *args , i )

'''
    for i in a :
         for j in b :
               for k in c :
                      ..... n of loop ...
                      return i,j,k,...,n
NOTE :
           maximum of n = 995
'''
def permut(*args) :
    if type(args[0]) != list:
        yield args
        return
    for i in args[0] :
        yield from permut(*args[1:] , i)
