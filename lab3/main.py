import numpy as np
import main_phase as m_ph

if __name__ == '__main__':
        ct=np.array([1,0,0])
        A=np.matrix([[1,1,1],[2,2,2]])
        b=np.array([[0],[0]])
        #print(b)
        #step 1
        #done

        #step 2
        n=np.size(ct)
        print("n",n)
        m=np.size(b)
        ct_overlined=np.zeros(shape=n+m)
        for i in range(n,n+m):
                ct_overlined[i]=-1
        print("ct_over\n",ct_overlined)

        A_overlined=np.hstack((np.array(A),np.eye(m)))
        print("A_over\n",A_overlined)

        #step 3
        x_overlined=np.hstack((np.zeros(n),b[:,0]))
        print("x_over\n",x_overlined)
        B=np.empty(shape=m)
        for i in range (n,n+m):
                B[i-n]=i+1
        print("B\n",B)

        #step 4
        while True:
                x_overlined, B, AAA_inv, ii, exx = m_ph.lab(ct_overlined, np.matrix(A_overlined), x_overlined, B)
                if exx:
                        print(x_overlined)
                        print(B)
                        break

        #step 5
        for i in range (n,n+m):
                if(x_overlined[i-n]!=0):
                        print("задача не совместна")
                        exit(0)

        #step 6
        xt=np.zeros(shape=n)

        #step 7
        if B.max()<=n and B.min()>0:
                print(x_overlined)
                print(B)
                exit(0)

        #step 8
        jk=B.max()
        print(jk)
        k=np.where(B==jk)[0][0]+1
        print(k)
        i=jk-n
        print(i)

        #step 7))
        j=np.arange(1,n+1)
        print(B)
        print(j)
        for p in j:
                if p in B:
                        j=j[j !=p]

        print(j)
        #l2=np.dot(AAA_inv,A[:,1])        #----------------
        #print(l2)
        #l3=np.dot(AAA_inv,A[:,2])        #---------------------
        #print(l3)
        #if(l2[k-1]!=0 or l3[k-1]!=0):   #--------------------
