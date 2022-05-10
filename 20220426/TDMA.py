#TDMA.py

import numpy
import matplotlib.pyplot as plt

def main():
    """
    以下pe~dxまで変更する
    """
    
    pe = 100.0      #ペクレ数
    phi2 = 50.0     #チーレ数
    N = 100         #計算点の数
    dt = 0.1        #Δt
    t_max = 100     #計算を止める時刻
    dx = 1.0 / N    #ΔX

    #3項方程式の係数
    a = []
    b = []
    c = []

    #3項方程式の係数の計算
    for i in range(N+1):
        temp_c = dt / (dx*dx)
        temp_a = temp_c + pe * (dt / dx)
        temp_b = temp_a + temp_c + phi2 * phi2 * dt + 1
        a.append(temp_a)
        b.append(temp_b)
        c.append(temp_c)

    a[N] = a[N] + c[N]    #i=Nでの境界条件

    #初期条件
    t = 0
    y = [0.0] * N
    d = [0.0] * N

    while t < t_max:
        #3項方程式の右辺の計算
        d[0] = a[0] * 1.0 + y[0]
        y = TDMA_Solve(a, b, c, d)
        #print(y)
        #print(t)
        plt.plot(y)
        plt.show()
        plt.clf()
        t = t + dt


def TDMA_Solve(a, b, c, d):
    p = [c[0]/b[0]]
    q = [d[0]/b[0]]

    for i in range(len(d)):
        p.append(c[i]/(b[i]-a[i]*p[i-1]))
        q.append((d[i]+a[i]*q[i-1])/(b[i]-a[i]*p[i-1]))

    y = [q[len(d)-1]]
    p.reverse()
    q.reverse()
    for i in range(len(d)-2):
        y.append(p[i]*y[i-1]+q[i])

    y.reverse()
    return y

if __name__ == '__main__':
    main()
