#Equation.py

import numpy as np
import matplotlib.pyplot as plt
import TDMA as tdma

def main():
    """
    以下pe~dxまで変更する
    """

    pe = 200.0      #ペクレ数
    phi2 = 50.0     #チーレ数
    N = 100         #計算点の数
    dt = 0.1        #Δt
    t_max = 20     #計算を止める時刻
    dx = 1.0 / N    #ΔX

    #3項方程式の係数
    a = []
    b = []
    c = []

    #3項方程式の係数の計算
    for i in range(N):
        temp_c = dt / dx**2
        temp_a = temp_c + pe * dt / dx
        temp_b = temp_a + temp_c + phi2 * dt + 1
        a.append(temp_a)
        b.append(temp_b)
        c.append(temp_c)

    a[N-1] = a[N-1] + c[N-1]    #i=Nでの境界条件

    #初期条件
    t = 0.0
    y = [0.0] * N
    d = [0.0] * N

    #グラフ横軸指定用
    x = [0.0] * N
    c_d = 1.0 / float(N)
    for i in range(1, N):
        x[i] = c_d * float(i)
    loop_n = 0  #グラフの描画回数指定用

    plt.figure(figsize=(8.5, 5))

    while t < t_max:
        #3項方程式の右辺の計算
        for num in range(len(y)):
            d[num] = y[num]

        d[0] = a[0] * 1.0 + y[0]
        _y = tdma.TDMA_Solve(a, b, c, d)
        if loop_n % 20 == 0:
            plt.plot(x, _y, label='t={}'.format(round(t, 1)))
        y = _y
        t = t + dt
        loop_n += 1
    plt.title('ΔX={}, ΔT={}, Pe={}, φ^2={}'.format(dx, dt, pe, phi2))
    plt.legend()
    plt.show()

if __name__ == '__main__':
        main()
