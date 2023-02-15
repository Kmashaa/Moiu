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
    #print("det",np.linalg.det(inv_A))
    return inv_A, x, i
def find_inverse_matrix(inv_A, x, i):

    if(np.linalg.det(inv_A)==0):
        raise LinAlgError("Singular matrix")


    n=len(inv_A)
    l=np.dot(inv_A,x)

    if(l[i,0]==0):
        raise LinAlgError("Singular matrix")

    l_tild = copy.copy(l)
    l_tild[i,0] = -1


    l_circ = -1/l[i,0] * l_tild

    Q=np.eye(n)
    Q[:,i]=l_circ[:,0]
    inv_A_overlined=np.zeros((n,n))
    for k in range(0,n):
        for j in range (0,n):
            if k!=i:
                inv_A_overlined[k,j]=Q[k,k]*inv_A[k,j]+Q[k,i]*inv_A[i,j]
            else:
                inv_A_overlined[k, j]=Q[k,k]*inv_A[k,j]
    return inv_A_overlined

def normal_method(inv_A,x,i):
    #print("inv_A",inv_A)
    A_test = np.linalg.inv(inv_A)
    #print("A_test",A_test)
    A_test[:, i] = x[:,0]
    #print("x",x)
    A_res = np.linalg.inv(A_test)
    #print(A_res)
    return A_res


def test_sing(j):
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


def test2(j):
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


def new_test(j):
    inv_A, x, i =input()

    try:
        a1=find_inverse_matrix(inv_A,x,i)
        #print(j,"my method counted")
    except Exception as ex:
        #print(j,"my method didn't counted")
        a1= type(ex).__name__
        #print("a1",j, a1)

    try:
        A_test = np.linalg.inv(inv_A)
        A_test[:, i] = x[:, 0]
        #print("A_test",A_test)
        a2= np.linalg.inv(A_test)
        #a2=normal_method(inv_A,x,i)
        #print(j,"normal method counted")
    except Exception as ex:
        #print(j,"normal method didn't counted")
        a2= type(ex).__name__
        #print("a2",j,a2)
        assert(a1==a2)
    else:

        assert(np.allclose(a1,a2))


if __name__ == '__main__':
    inv_A, x, i= input()
    AA=find_inverse_matrix(inv_A,x,i)
    AAA=normal_method(inv_A,x,i)

    #for j in range(500):
    #    test_sing(j)
    #straight_method(inv_A,x,i)
    for k in range(50000):
        test2(k)



