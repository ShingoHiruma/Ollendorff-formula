import numpy as np
import math
import cmath
import matplotlib.pyplot as plt

# 描画範囲の指定
# omega = np.arange(x軸の最小値, x軸の最大値, 刻み)
freq = np.arange(1, 1e4, 1)
omega = freq*2*np.pi
width = np.arange(0.001,0.006,0.001)

def dot_mur(mu_r,z):
    return (cmath.tan(z)/z)

fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4), sharex=True)
fig2, (axL2, axR2) = plt.subplots(ncols=2, figsize=(10,4), sharex=True)
for d in width:
    # 計算式
    # 導電率
    sigma = 1.00e5
    # 透磁率
    mu_r = 1000.0
    mu_0 = 4.0*np.pi*1.0e-7


    z = [cmath.sqrt(-1j*x*mu_r*mu_0*sigma*d*d) for x in omega]
    dot_mu_real = [dot_mur(mu_r,zi).real for zi in z]
    dot_mu_imag = [dot_mur(mu_r,zi).imag for zi in z]
    impedance_real = [mu_0*(1j*x*dot_mur(mu_r,zi)).real for zi, x in zip(z,omega)]
    impedance_imag = [mu_0*(1j*x*dot_mur(mu_r,zi)).imag for zi, x in zip(z,omega)]
    # 横軸の変数。縦軸の変数
    axL.plot(freq, dot_mu_real, label="d="+str(d))
    axR.plot(freq, dot_mu_imag, label="d="+str(d))
    axL2.plot(freq, impedance_real, label="d="+str(d))
    axR2.plot(freq, impedance_imag, label="d="+str(d))

axL.set_xlim(1,1e4)
axL.set_xlabel("Frequency [Hz]")
axL.set_ylabel("Real part of complex permeability")
axL.set_xscale('log')
axL.legend()

axR.set_xlabel("Frequency [Hz]")
axR.set_ylabel("Imaginary part of complex permeability")

axL2.set_xlim(1,1e4)
axL2.set_xlabel("Frequency [Hz]")
axL2.set_ylabel("Real part of impedance")
axL2.set_xscale('log')
axL2.set_yscale('log')
axL2.legend()

axR2.set_xlabel("Frequency [Hz]")
axR2.set_ylabel("Imaginary part of impedance")
axR2.set_yscale('log')
axR2.legend()
# axR.legend()
# 描画実行
plt.show()