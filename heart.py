# draw heart
def d(s): # s = str() --> len(s) = 1
    print(' '*10,s*4+' '*7+s*4)
    for i in range(5,0,-2):
        print(' '*9,s*(7-i//2+1)+' '*i+s*(7-i//2+1))
    for i in range(17,0,-2):
        print(' '*(17-i//2),s*i)
