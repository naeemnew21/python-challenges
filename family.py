
        
class human:
    '''
       this class is a tree
       parent > child
       name : name of person
       self_object : name of variable(child) as a string
       parent : object that inherit from
    '''
    children = 0
    def __init__(self , name  , self_object ,parent = None , data = dict() ) :
        try :
            parent.children += 1
            self.parent = parent
            self.parent.son[name] = self_object
            
            self.name = parent.name[:]
            self.name.append(name)
            self.data = data
            
            self.son = dict()
        except :
            self.name = [name]
            self.son = dict()

    def __str__(self) :
        return ''.join(i+' ' for i in self.name[::-1])


    def brother(self) :
        try :
            brothers = self.parent.son.copy()
            del(brothers[self.name[-1]])
            return brothers  # return dict()  brother_name : variable
        except :
            return None


    def uncel(self) :
        try :
            return self.parent.brother # return dict()  uncel_name : variable
        except :
            return None


def broth(a , b) :
    return a.name[:-1] == b.name[:-1] 

def fath(father , son) :
    return son.name[:-1] == father.name

def grandfa(grand , son) :
    return son.name[:-2] == grand.name

def as_grandfa(grand , son) :
    if grandfa(grand , son) :
        return False
    return (grand.name[0] == son.name[0]) and (len(grand.name) == len(son.name)-2)

def unc(uncel , son) :
    return uncel.name[:-1] == son.name[:-2]

def as_unc(uncel , son) :
    if fath(uncel,son) or unc(uncel,son):
        return False        
    return (uncel.name[0] == son.name[0]) and (len(uncel.name) == len(son.name)-1)

def cousin(mem , cos) :
    return mem.parent.parent.name == cos.parent.parent.name

def get_cousins(me):
    cos = dict()
    for i in me.parent.brother :
        x = me.parent.parent.son[i]
        cos[i] = []
        for j in eval(x).son :
            cos[i].append(j)
    return cos


# x = []
# x.append( human('name' , str( len(x) ) , parent = x[index]) )

naeem = human('naeem' , 'naeem')
ali = human('ali' , 'ali' , naeem)
mah = human('mahmoud' ,'mah' , ali)
moh = human('mohammed' , 'moh' , mah)
mah2 = human('mahmoud' , 'mah2' , moh)
moh2 = human('mohammed' , 'moh2' , moh)
ahm = human('ahmed' , 'ahm' , moh)
hel = human('helmy' , 'hel ' , mah)
maher = human('maher' , 'maher' , hel)
moh3 = human('mohammed', 'moh3' , hel)
ahm2 = human('ahmed' , 'ahm2' , maher)


