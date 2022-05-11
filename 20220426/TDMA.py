#TDMA.py

import numpy
import matplotlib.pyplot as plt

def main():
    a=[0.0, 1.0, 2.0, 3.0, 4.0]
    b=[1.0, 2.0, 3.0, 4.0, 5.0]
    c=[1.0, 1.0, 1.0, 1.0, 0.0]
    d=[2.0, 4.0, 6.0, 8.0, 10.0]
    y=TDMA_Solve(a,b,c,d)
    print(y)


def TDMA_Solve(a, b, c, d):
    p = [c[0]/b[0]]
    q = [d[0]/b[0]]
    for i in range(1, len(d)):
        p.append(c[i]/(b[i]-a[i]*p[i-1]))
        q.append((d[i]+a[i]*q[i-1])/(b[i]-a[i]*p[i-1]))

    y = [0.0]*len(d)
    y[len(d)-1] = q[len(d)-1]
    for i in range(len(d)-2, -1, -1):
        y[i] = p[i]*y[i+1]+q[i]

    return y

if __name__ == '__main__':
    main()
