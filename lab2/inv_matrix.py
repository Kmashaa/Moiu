import numpy as np
import copy
from numpy.linalg import LinAlgError

def input():
    n = np.random.randint(2, 10)
    i = np.random.randint(0, n)
    inv_A = np.random.randint(1,10, size=(n, n))
    while(True):
        if(int(np.linalg.det(inv_A))==0):
            inv_A = np.random.randint(1, 10, size=(n, n))
        else:
            break
    x = np.random.randint(10, size=(n, 1))
    return inv_A, x, i

def find_inverse_matrix(inv_A, x, i):

    if(np.linalg.det(inv_A)==0):
        raise LinAlgError("Singular matrix")

    #1 step
    n=len(inv_A)
    l=np.dot(inv_A,x)

    if(l[i,0]==0):
        raise LinAlgError("Singular matrix")
    #2 step
    l_tild = copy.copy(l)
    l_tild[i,0] = -1

    #3 step
    l_circ = -1/l[i,0] * l_tild

    #4 step
    Q=np.eye(n)
    Q[:,i]=l_circ[:,0]

    #5 step
    inv_A_overlined=np.zeros((n,n))
    for k in range(0,n):
        for j in range (0,n):
            if k!=i:
                inv_A_overlined[k,j]=Q[k,k]*inv_A[k,j]+Q[k,i]*inv_A[i,j]
            else:
                inv_A_overlined[k, j]=Q[k,k]*inv_A[k,j]
    return inv_A_overlined

def normal_method(inv_A,x,i):
    A_test = np.linalg.inv(inv_A)
    A_test[:, i] = x[:,0]
    A_res = np.linalg.inv(A_test)
    return A_res


def test_sing():
    inv_A, x, i=input()
    x = np.random.randint(1, size=(len(inv_A), 1))
    try:
        AA=find_inverse_matrix(inv_A,x,i)
    except Exception as ex:
        AA = type(ex).__name__
    try:
        AAA = normal_method(inv_A, x, i)
    except Exception as ex:
        AAA = type(ex).__name__
    assert(AA==AAA)


def test():
    array, x, i = input()
    try:
        result1 = find_inverse_matrix(array, x, i)
    except Exception as ex:
        result1 = type(ex).__name__
    try:
        result2 = normal_method(array, x, i)
    except Exception as ex:
        result2 = type(ex).__name__
        assert(result1 == result2)
    else:
        #print(result1)
        #print(result2)
        assert(np.allclose(result1, result2))





if __name__ == '__main__':
    inv_A, x, i= input()
    AA=find_inverse_matrix(inv_A,x,i)
    AAA=normal_method(inv_A,x,i)

    for j in range(500):
        test_sing()
    for k in range(500):
        test()




