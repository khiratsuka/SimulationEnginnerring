#TwoComp_Equation.py

import numpy as np
import matplotlib.pyplot as plt
import TDMA as tdma

def main():
    """
    L11-18まで変更可
    """
    phi2 = 200.0     #チーレ数
    N = 100         #計算点の数
    dt = 0.01       #Δt
    gamma = 0.8     #DB/DA
    theta = 10.0    #CB/CA
    eps = 1e-3      #収束判定指数
    t_max = 100     #計算を止める時刻
    dx = 1.0 / N    #ΔX

    #3項方程式の係数
    aa = []
    ca = []
    ab = []
    cb = []

    #3項方程式の係数の計算
    for i in range(N):
        temp_aa_ca = dt / dx**2
        temp_ab_cb = gamma * dt / dx**2
        aa.append(temp_aa_ca)
        ca.append(temp_aa_ca)
        ab.append(temp_ab_cb)
        cb.append(temp_ab_cb)

    aa[N-1] = aa[N-1] + ca[N-1]    #i=Nでの境界条件
    ab[N-1] = ab[N-1] + cb[N-1]

    #初期条件
    t = 0.0
    ya = [1.0] * N
    yb = [0.0] * N
    for i in range(int(N/2), N):
        ya[i] = 0.0
        yb[i] = 1.0
    da = [0.0] * N
    db = [0.0] * N
    yba = [0.0] * N
    ba = [0.0] * N
    bb = [0.0] * N
    errors = [0.0] * N
    

    #グラフ横軸指定用
    x = [0.0] * N
    c_d = 1.0 / float(N)
    for i in range(1, N):
        x[i] = c_d * float(i)
    loop_n = 0  #グラフの描画回数指定用

    plt.figure(figsize=(8.5, 5))

    eps_bool = True
    while t < t_max:
        for num in range(N):
            da[num] = ya[num]
            db[num] = yb[num]
        
        while eps_bool:
            for i in range(N):
                yba[i] = yb[i]
                ba[i] = aa[i] + ca[i] + 1 + theta * phi2 * yba[i]
            ya = tdma.TDMA_Solve(aa, ba, ca, da)
            for j in range(N):
                bb[j] = 1.0 + ab[j] + cb[j] + phi2 * ya[j]
            yb = tdma.TDMA_Solve(ab, bb, cb, db)
            for ne in range(N):
                errors[ne] = abs(yb[ne] - yba[ne]) / yb[ne]
            print("error:{}, eps:{}".format(max(errors), eps))
            if max(errors) < eps:
                eps_bool = False
        t = t + dt
        loop_n += 1
    
    plt.title('φ^2={}, θ={}, Γ={}'.format(phi2, theta, gamma))
    plt.plot(x, ya, label="$Y_{A}$")
    plt.plot(x, yb, label="$Y_{B}$")
    plt.legend()
    plt.show()

if __name__ == '__main__':
        main()
