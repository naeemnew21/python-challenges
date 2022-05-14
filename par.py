# test if hte parents identical or no
def test(string , x = '[]{}()', ) :
    s = str().join([i for i in string if i in x])
    for i in range(len(s)//2) :
        for r in range(0, len(x)-1 , 2) :
            s = s.replace(x[r]+x[r+1],'')
    return len(s) == 0
