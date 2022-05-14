

def count_char(text) :
    dic = {i : 0 for i in text if i != ' '}
    for i in text.replace(' ','') :
        dic[i] += 1
    return dic


def count_char(text) :
    dic = {i : 0 for i in text if i != ' '}
    for i in text.replace(' ','') :
        dic[i] = text.count(i)
    return dic


import collections
def count_char(text) :
    a = list(text.replace(' ' ,''))
    return collections.Counter(a)

if __name__ == '__main__' :

    x = 'google test'
    y = count_char(x)
    for i in  y :
        print('{} : {}'.format(i , y[i]) )
