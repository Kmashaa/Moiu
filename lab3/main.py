import numpy as np
import main_phase as m_ph


def test1():
        ct = np.array([1, 0, 0])
        A = np.matrix([[1, 1, 1], [2, 2, 2]])
        b = np.array([[0], [0]])
        x_expexted=np.array([0,0,0])
        B_expected=np.array([1])
        x, B = initial_phase(ct, A, b)
        if (x_expexted != x).any() or (B_expected != B).any():
                print("test failed")

        else:
                print("test passed successful")


def initial_phase(ct,A,b):
        # step 1
        for s in range(0,np.size(b)):
                if b[s]<0:
                        b[s]*=-1
                        A[s,:]*=-1

        # step 2
        n = np.size(ct)

        m = np.size(b)
        ct_overlined = np.zeros(shape=n + m)
        for i in range(n, n + m):
                ct_overlined[i] = -1


        A_overlined = np.hstack((np.array(A), np.eye(m)))


        # step 3
        x_overlined = np.hstack((np.zeros(n), b[:, 0]))

        B = np.empty(shape=m)
        for i in range(n, n + m):
                B[i - n] = i + 1

        # step 4
        while True:
                x_overlined, B, AAA_inv, ii, exx = m_ph.lab(ct_overlined, np.matrix(A_overlined), x_overlined, B)
                if exx:
                        break

        # step 5
        for i in range(n, n + m):
                if (x_overlined[i - n] != 0):
                        print("задача не совместна")
                        exit(0)

        # step 6
        xt = np.zeros(shape=n)




        while True:
                # step 7
                if B.max() <= n and B.min() > 0:
                        return xt, B

                # step 8
                jk = B.max()

                k = np.where(B == jk)[0][0] + 1

                i = jk - n


                # step 7))
                j = np.arange(1, n + 1)

                counter = 0
                for p in j:
                        if p in B:
                                j[counter] = 0
                        counter += 1


                l = np.zeros((np.size(AAA_inv[:, 0]), np.size(j)))

                l = np.matrix(l)

                counter = 0
                for p in j:
                        if p != 0:
                                l[:, counter] = np.dot(AAA_inv, A[:, counter])
                        counter += 1

                # step 8

                for p in j:
                        if p != 0:
                                if l[k - 1, p - 1] != 0:
                                        B[int(j[int(i - 1)]) - 1] = p

                # step 9
                chk = False
                counter1 = 0
                counter2 = 0
                for p in j:
                        if p != 0:
                                counter1 += 1
                                if l[k - 1, p - 1] == 0:
                                        counter2 += 1
                if counter1 == counter2:
                        A = np.delete(A, int(i - 1), axis=0)
                        A_overlined = np.delete(A_overlined, int(i - 1), axis=0)
                        b = np.delete(b, int(i - 1), axis=0)
                        B = np.delete(B, int(j[int(i - 1)]) - 1, axis=0)



if __name__ == '__main__':
        # ct=np.array([1,0,0])
        # A=np.matrix([[1,1,1],[2,2,2]])
        # b=np.array([[0],[0]])
        # x,B = initial_phase(ct,A,b)
        # print("x=",x,"B=",B)
        test1()