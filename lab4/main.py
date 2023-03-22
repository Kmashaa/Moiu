import numpy as np

def test1():
    cc = np.array([-4, -3, -7,0,0])
    AA = np.matrix([[-2, -1, -4, 1, 0], [-2,-2,-2,0,1]])
    bb = np.array([[-1], [-3/2]])
    BB=np.array([4,5])
    k_expected=np.array([0.25,0.5,0,0,0])
    k=dual_simplex_method(cc,AA,bb,BB)
    if (k_expected != k).any():
        print("test failed")
    else:
        print("test passed successful")

def dual_simplex_method(ct,A,b,B):
    n=np.size(ct)
    while True:
        #step 1
        AB = np.matrix(np.zeros(shape=(np.size(A[:, 0]), np.size(B))))
        for i in range (np.size(B)):
            AB[:,i]=A[:,int(B[i]-1)]
        AB_inv=np.linalg.inv(AB)

        #step 2
        cbt=np.empty(shape=np.size(B))
        for i in range (np.size(cbt)):
            cbt[i]=ct[B[i]-1]


        #step 3
        yt=np.dot(cbt,AB_inv)


        #step 4
        kb=np.dot(AB_inv,b)
        kt=np.zeros(shape=n)
        for j in range (np.size(B)):
            kt[B[j]-1]=kb[j]


        #step 5
        counter=0
        for i in range (np.size(kt)):
            if kt[i]>=0:
                counter+=1
        if counter==np.size(kt):
            return kt

        #step 6
        k_ind_j=0
        for i in range(np.size(kt)):
            if kt[i]<0:
                k_ind_j=np.where(B==i+1)[0][0]+1
                continue
            elif kt[i]>=0:
                continue


        #step 7
        dy=AB_inv[k_ind_j-1,:]
        mu=np.zeros(shape=n)
        for j in range (n):
            if j+1 not in B:
                mu[j]=np.dot(dy,A[:,j])


        #step 8
        for j in range (np.size(mu)):
            if(mu[j])<0 and j+1 not in B :
                break
            elif j==np.size(mu)-1 and j+1 not in B:
                exit("задача не совместна")


        #step 9
        delta=np.zeros(shape=np.size(mu))
        for j in range (np.size(mu)):
            if(mu[j])<0 and j+1 not in B:
                delta[j]=(ct[j]-int(np.dot(np.transpose(A[:,j]),np.transpose(yt))))/mu[j]


        #step 10
        delta_temp=np.empty(shape=0)
        for j in range(np.size(delta)):
            if j not in B and mu[j]<0:
                delta_temp=np.append(delta_temp,delta[j])
        delta0=np.min(delta_temp)
        j0=np.where(delta==delta0)[0][0]+1


        #step 11
        B[k_ind_j-1]=j0

if __name__ == '__main__':
    test1()