import numpy as np
import copy
from numpy.linalg import LinAlgError
def input():
    n = np.random.randint(2, 10)
    i = np.random.randint(0, n)
    inv_A = np.random.randint(10, size=(n, n))
    x = np.random.randint(10, size=(n, 1))
    print(x)
    return inv_A, x, i
def find_inverse_matrix(inv_A, x, i):
    n=len(inv_A)
    l=np.dot(inv_A,x)

    if(l[i,0]==0):
        raise LinAlgError("Singular matrix")

    l_tild = copy.copy(l)
    l_tild[i,0] = -1

    l_circ = -1/(l[i,0]) * l_tild

    E_n=np.eye(n)
    Q=copy.copy(E_n)
    Q[:,i]=l_circ[:,0]

    inv_A_overlined=np.zeros((n,n))
    for k in range(0,n):
        for j in range (0,n):
            inv_A_overlined[k,j]=Q[k,k]*inv_A[k,j]+Q[k,i]*inv_A[i,j]
            if(i==k):
                inv_A_overlined[k, j]/=2
    return inv_A_overlined

def normal_method(inv_A,x,i):
    try:
        A_test = np.linalg.inv(inv_A)
    except Exception as ex:
        res2 = type(ex).__name__
        #print(res2)
        return res2
    else:
        A_test[:, i] = x
        try:
            A_res = np.linalg.inv(A_test)
        except Exception as ex:
            res2 = type(ex).__name__
            print(res2)
            return res2
        else:
            return A_res

def test_sing():
    inv_A, x, i=input()
    x=np.zeros(len(inv_A)).astype(int)
    try:
        AA=find_inverse_matrix(inv_A,x,i)
    except Exception as ex:
        AA = type(ex).__name__
    try:
        AAA = normal_method(inv_A, x, i)
    except Exception as ex:
        AA = type(ex).__name__
    assert(AA==AAA)

def test():
    inv_A, x, i=input()
    try:
        res1=find_inverse_matrix(inv_A,x,i)
    except Exception as ex:
        res1 = type(ex).__name__
        #print("AA",AA)
    try:
        res2 = normal_method(inv_A, x, i)
    except Exception as ex:
        res2 = type(ex).__name__
        #print(AAA)
        #print(ex)
        assert(res1==res2)
    else:
        #print(res1)
        #print(res2)
        assert(np.allclose(res1,res2))


if __name__ == '__main__':
    inv_A, x, i= input()
    AA=find_inverse_matrix(inv_A,x,i)
    AAA=normal_method(inv_A,x,i)

    test_sing()
    for j in range(50):
        test()



