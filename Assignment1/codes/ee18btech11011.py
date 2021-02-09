import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex

x = [1,2,3,4,2,1]
N = len(x)
M = 2*N

def h(M):
	h = []
	for i in range(M):
		output = 0;
		if i >= 0:
			output += (-1/2)**i
		if i-2 >= 0:
			output += (-1/2)**(i-2)
		h.append(output)		
	return h

h = h(M)

def DFT(f):
	F = []
	N = len(f)
	for k in range(N):
		output = complex(0)
		for n in range(N):
			tmp = -1j*2*np.pi*k*n/N
			output += f[n]*np.exp(tmp)
		F.append(output)
	return F
	
print ("DFT of x(n)\n",DFT(x))
print()
print ("DFT of h(n)\n",DFT(h))

plt.figure(figsize=(12,12))
plt.subplot(3,2,1)
plt.stem(range(0,N),x)
plt.title('$x(n)$')
plt.grid()

plt.subplot(3,2,2)
plt.stem(range(0,M),h)
plt.title('$h(n)$')
plt.grid()

plt.subplot(3,2,3)
plt.stem(range(0,N),np.abs(DFT(x)))
plt.title('$|DFT(x)|$')
plt.grid()

plt.subplot(3,2,4)
plt.stem(range(0,N),np.angle(DFT(x)))
plt.title('$phase(DFT(x))$')
plt.grid()

plt.subplot(3,2,5)
plt.stem(range(0,M),np.abs(DFT(h)))
plt.title('$|DFT(h)|$')
plt.grid()

plt.subplot(3,2,6)
plt.stem(range(0,M),np.angle(DFT(h)))
plt.title('$phase(DFT(h))$')
plt.grid()

#If using termux
plt.savefig('../figs/figs.pdf')
plt.savefig('../figs/figs.eps')
subprocess.run(shlex.split("termux-open ../figs/figs.pdf"))
#else
#plt.show()
