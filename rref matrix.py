A = [
     [3,1,2,1,0,0],
     [2,1,2,0,1,0],
     [1,2,2,0,0,1]
     ]



def zero(R1, R2):
    '''>>>to make element under pivot in R1 
        equal Zero
       >>> pivot in R1 must equal 1
    '''
    col = R1.index(1) # pivot coloumn
    update_R1 = [-i*R2[col] for i in R1]
    update_R2 = [i+j for i,j in zip(update_R1 , R2)]
    return update_R2
     

def check_pivots(R,A):
    'check if pivot in R , pivot in R must equal 1'
    pivot = R.index(1) # index of pivot
    for row in A :
        for i in row[:pivot] :
            if i != 0:
                return False
    else :
        return True


def one_pivot(R) :
    pivot = 0
    for i in R :
        if i != 0 :
            pivot = i
            break
    if pivot == 0 :
        return [0 for i in R]
    return [i/pivot for i in R]


def init_mat(A) :
    update_first_row = one_pivot(A[0])      
    if check_pivots( update_first_row , A[1:]) :
        return True
    else :
        mat = A[1:]
        mat.append(A[0])
        return mat       # interchange rows, make the first row in the last
    
def get_final_mat(A) :
    new_mat = init_mat(A)
    if new_mat == True:
        return A
    return get_final_mat(new_mat)



def forward_elim(A):
    update_A = [one_pivot(A[0])]
    for row in A[1:] :
        update_row = zero(update_A[0] , row)
        update_A.append(update_row)
    return update_A


def backward_elim(A):
    update_A = []
    for row in A[:-1] :
        update_row = zero(A[-1] , row)
        update_A.append(update_row)
    update_A.append(A[-1])
    return update_A



def get_ref(A) :
    update_A = A
    for i in range(len(A)) :
        mat = get_final_mat(update_A[i:])
        update_A = update_A[:i]+ forward_elim(mat)
    return update_A
            

def get_rref(A) :           
    update_A = get_ref(A)
    for i in range(len(A)) :
        update_A = backward_elim(update_A[:len(A)-i]) + update_A[len(A)-i:]
    return [[round(n , 2) for n in row] for row in update_A]