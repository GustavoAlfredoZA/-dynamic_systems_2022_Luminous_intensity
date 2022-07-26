import numpy as np
import pandas as pd
import math
import scipy.constants as constant
import matplotlib.pyplot as plt

def S_v(v,data,index):
    T = data.iloc[index,1]
    r1 = 2*constant.h*v**3/constant.c**2
    r2 = 1/(math.e**(constant.h*v/constant.k*T)-1)
    return r1*r2

def opacidad(data,index,i=1,Z=[1],v = 1.7e+10):
    T = data.iloc[index,1]
    k_v = 0
    n_e = data.iloc[index,2]
    r1 = 9.78*10e-3
    r2 = n_e/(v**2*T**(3/2))
    r3 = 0
    for j in range(1):
        r3 += Z[j]**2*data.iloc[j,2]
    if T<2*10e5:
        r4 = 18.2 + np.log(T**(3/2))-np.log(v)
    else:
        r4 = 24.5 + np.log(T)-np.log(v)
    k_v = r1 * r2 * r3 * r4
    return k_v

def T_v(a,dx,data,index, i):
    return (dx/2)*(opacidad(data,index,a)+opacidad(data,index,a+dx))

def I_v(data, index):
    R = data.iloc[index,3] * math.exp(-data.iloc[index,2])+S_v(data=data,index=index,v=1-math.exp(-data.iloc[index,2]))
    return R

data = pd.read_csv('data1.csv')

print(data.head())

data = data[['h','T','n_e']]
print(data.head())

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(10,6))

ax1.plot(data['h'],data['T'])
ax1.set_ylabel('Temperature T  [K]')
ax1.set_xlabel('Height h [km]')

ax2.plot(data['h'],data['n_e'])
ax2.set_ylabel('Electron number density [cm^-3]')
ax2.set_xlabel('Height h [km]')

v= 1.7e+10
I_0 = 0,0

data['t']=0
data['I']=0
data.iloc[0,3]=0
for i in range(data.shape[0]):
    a = data.iloc[i,0]
    dx = data.iloc[i,0]-data.iloc[min(51+1,data.shape[0]-1),0]
    data.iloc[i,3] = T_v(a=a,dx=dx,data=data,index=i,i=1)
    data.iloc[i,4] = I_v(data,index = i)


print(data)

ax3.plot(data['h'],data['t'])
ax3.set_ylabel('Optical depth t')
ax3.set_xlabel('Height h [km]')

ax4.plot(data['h'],data['I'])
ax4.set_ylabel('Luminous intensity I  [erg/cm^2 sec Hz srad]')
ax4.set_xlabel('Height h [km]')

plt.show()
plt.savefig('examen_SD.png')
