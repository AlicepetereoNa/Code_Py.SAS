#离散时间信号的卷积和运算
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
def uDt(n):
    if n>=0:
        y=1
    else:
        y=0
    return y
nx=np.linspace(-1,5,7,dtype=int,endpoint=True)
nh=np.linspace(-2,10,13,dtype=int,endpoint=True)
nx2=nx-4
nh2=nh-9
x=np.array([uDt(i)for i in nx])-np.array([uDt(i)for i in nx2])
h=np.power(0.9,nh)
h1=np.array([uDt(i)for i in nh])-np.array([uDt(i)for i in nh2])
y=np.convolve(h,h1)
ny1=nx[0]+nh[0]
ny=ny1+np.linspace(0,(len(y)),len(y),dtype=int)
fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax1.stem(nx,x)
ax1.grid(visible=True)
ax1.set_title('x(n)')
ax1.axis([-4,16,0,1.5])
ax2=fig.add_subplot(3,1,2)
ax2.stem(nh,h)
ax2.grid(visible=True)
ax2.set_title('h(n))')
ax2.axis([-4,16,0,1.5])
ax3=fig.add_subplot(3,1,3)
ax3.stem(ny,y)
ax3.set_title('y(n)')
ax3.grid(visible=True)
ax3.axis([-4,16,0,9])
plt.show()