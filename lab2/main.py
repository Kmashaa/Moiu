
import inv_matrix as inv
import numpy as np

def start_tests():
    test1()
    test2()
    test3()
    print("all tests passed successful")
def test1():
    cc = np.array([[1], [1], [0], [0], [0]])
    AA = np.matrix([[-1, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]])
    xx = np.array([[0], [0], [1], [3], [2]])
    jj = np.array([3, 4, 5])
    expected_res=np.array([[3],[2],[2],[0],[0]])

    while True:
        xx,jj,AAA_inv,ii,exx=lab(cc,AA,xx,jj)
        if exx:
            if(expected_res!=xx).any():
                print("test failed")
                break
            else:
                print("test passed successful")
                break

def test2():
    cc = np.array([[1], [0], [0], [0]])
    AA = np.matrix([[-1, 0, 1, 0], [0, -1, 0, 1]])
    xx = np.array([[1], [1], [0], [0]])
    jj = np.array([1, 2])
    while True:
        xx, jj, AAA_inv, ii, exx = lab(cc, AA, xx, jj)
        if exx:
            print("test passed successful")
            break

def test3():
    cc = np.array([[20],
                  [25],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0]])
    AA = np.matrix([[1, 2, 1, 0, 0, 0, 0, 0],
                  [2, 1, 0, 1, 0, 0, 0, 0],
                  [-1, 0, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 1, 0, 0],
                  [0, -1, 0, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 1]])
    xx = np.array([[0],
                  [0],
                  [10],
                  [11],
                  [0],
                  [5],
                  [0],
                  [4]])
    jj = np.array([3,4,5,6,7,8])
    expected_res=np.array([[4], [3], [0],[0],[4],[1],[3],[1]])
    while True:
        xx, jj, AAA_inv, ii, exx = lab(cc, AA, xx, jj)
        if exx:
            if (expected_res != xx).any():
                print("test failed")
                print(xx)
                print(expected_res)
                break
            else:
                print("test passed successful")
                break

def lab(c,A,x,j,A_inv=None,ii=None):
    ct=np.transpose(c)
    #step 1
    if isinstance(A_inv,type(None)):
        AB = np.matrix(np.zeros(shape=(np.size(A[:, 0]), np.size(j))))
        for i in range (np.size(j)):
            AB[:,i]=A[:,j[i]-1]

        AB_inv=np.linalg.inv(AB)
    else:
        xx=np.array(A[:,j[ii]-1])
        AB_inv=inv.find_inverse_matrix(np.array(A_inv),xx,ii)

    #step 2
    cb=np.empty(shape=np.size(j))
    for i in range(np.size(j)):
        cb[i]=c[j[i]-1]

    cbt=np.transpose(cb)

    #step 3
    ut=np.dot(cbt,AB_inv)

    #step 4
    lambt=np.dot(ut,A)-ct

    #step 5
    if(int(np.amin(lambt))>=0):
        return x, j, AB_inv, i, 1

    #step 6
    j0=(np.where(lambt==np.amin(lambt))[1][0])+1

    #step 7
    z=np.dot(AB_inv,A[:,j0-1])

    #step 8
    tettat=np.zeros(np.size(z))

    ind=0
    for zet in np.nditer(z):
        if zet<=0:
            tettat[ind]=float('inf')
        elif zet > 0:
            tettat[ind]=float(x[j[ind]-1])/float(z[ind])
        ind+=1


    #step 9
    tetta0=np.amin(tettat)

    #step 10
    if float(tetta0)==float('inf'):
        print("целевой функционал задачи не ограничен сверху на множестве допустимых планов")
        return x, j, AB_inv, 1, 1

    #step 11
    k=np.where(tettat==tetta0)[0][0]

    #step 12
    jst=j[k]
    j[k]=j0

    #step 13
    x[j0-1]=float(tetta0)

    for i in range(np.size(j)):
        if i !=k:
            x[j[i]-1]=x[j[i]-1]-tetta0*z[i]

    x[jst-1]=0
    return x, j, AB_inv, k, 0



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    start_tests()






















