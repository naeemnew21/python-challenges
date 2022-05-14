# combination


def combs(lst , n , *args) :
    if type(n) != int or n < 0 :
        raise TypeError('n must be integer >= 0')
        
    if n == 0 :
        yield args
        return
    for i , c in zip(lst[:-(n-1)] if n > 1 else lst  , range(len(lst))):
        yield from combs(lst[c+1:] , n-1 , *args , i )
