'''
sudoko anser

[a , b , c]
[d , e , f ] 
[g , h , i ]

given : collection of numbers from (a - i) provided that the collection is squared
              ex : 2*2 , 3*3 , .....
required : the correction order for given numbers to satisfy
                    the next relations :
                    1 : sum of any row = n
                    2 : sum of any column = n
                    2 : sum of the two crosses = n
rules :
           you can't repeat any number
solution :
             solution = Ans(start , end , step , n)
             start : the smallest number
             end : the biggest number
             step : the difference between any two sequential numbers
             n : sum of any column or row or cross
             
ex : collection >> (1 - 9) ,  n = 15
solution :
                 solution = Ans(1 , 10 , 1 , 15)
'''
from itertools import combinations , permutations

def perm(start , end , step , collection , n) :
    return [i for i in permutations(range(start, end , step) , collection) if sum(i) == n]

def sumColAndCross(i):
    summ = []    
    '''sum columns '''
    for count in range(len(i)) :
        summ.append(sum([e[count] for e in i]))        
    '''sum cross '''
    summ.append(sum(e[n] for e,n in zip(i , range(len(i)))))  
    summ.append(sum(e[n] for e,n in zip(i , range(len(i)-1 , -1 , -1))))    
    return summ

def setSimilar(i):
    for block in combinations(i , 2) :
        if set(block[0]).intersection(set(block[1])) :
            return True

def Ans(start = 1 , end = 10 , step = 1  , n = 15) :
    collection = int((end - start)**(0.5))  # len of row or column
    for i in permutations(perm(start , end , step, collection , n) , collection) :

        '''make sure that no element is repeated '''
        if setSimilar(i) :
            continue

        '''get sum of columns and cross , sigma = [sum(col 1) ,
            sum(col 2) , ... ,sum(col n), sum(cross 1) , sum(cross(2))] '''
        sigma = sumColAndCross(i)        
        if min(sigma) == max(sigma) == n  :
            return i
