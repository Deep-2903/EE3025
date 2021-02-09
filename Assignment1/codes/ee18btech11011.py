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

fig , ax = plt.subplots(nrows = 3, ncols = 2, figsize=(10,12))

ax[0][0].stem(range(0,N),x)
ax[0][0].set_title(r'$x(n)$')
ax[0][0].grid()

ax[0][1].stem(range(0,M),h)
ax[0][1].set_title(r'$h(n)$')
ax[0][1].grid()

ax[1][0].stem(range(0,N),np.abs(DFT(x)))
ax[1][0].set_title(r'$|DFT(x)|$')
ax[1][0].grid()

ax[1][1].stem(range(0,N),np.angle(DFT(x)))
ax[1][1].set_title(r'$phase(DFT(x))$')
ax[1][1].grid()

ax[2][0].stem(range(0,M),np.abs(DFT(h)))
ax[2][0].set_title(r'$|DFT(h)|$')
ax[2][0].grid()

ax[2][1].stem(range(0,M),np.angle(DFT(h)))
ax[2][1].set_title(r'$phase(DFT(h))$')
ax[2][1].grid()

#If using termux
plt.savefig('../figs/figs.pdf')
plt.savefig('../figs/figs.eps')
subprocess.run(shlex.split("termux-open ../figs/figs.pdf"))
#else
#plt.show()
