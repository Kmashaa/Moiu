import numpy as np
import copy

def find_inverse_matrix(inv_A, x, i):
    l=np.dot(inv_A,x)

    if(l[i,0]==0):
        return 0

    l_tild = copy.copy(l)
    l_tild[i,0] = -1

    l_circ = -1/float(l[i,0]) * l_tild

    E_n=np.eye(n)
    Q=copy.copy(E_n)
    Q[:,i]=l_circ[:,0]

    inv_A_overlined=np.zeros((n,n))
    for k in range(0,n):
        for j in range (0,n):
            inv_A_overlined[k,j]=Q[k,k]*inv_A[k,j]+Q[k,i]*inv_A[i,j]
            if(i==k):
                inv_A_overlined[k, j]/=2
    #print(inv_A_overlined)
    return inv_A_overlined



if __name__ == '__main__':
    n = np.random.randint(2, 5)
    i = np.random.randint(1, n)
    inv_A = np.random.randint(10, size=(n, n))
    x = np.random.randint(10, size=(n, 1))

    AA=find_inverse_matrix(inv_A, x, i)

    A_test=np.linalg.inv(inv_A)
    A_test[:,i]=x[:,0]
    A_res=np.linalg.inv(A_test)
    print(A_res)
    print(AA)



