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

def DFT(s):
	S = []
	N = len(s)
	for k in range(N):
		o = 0 * 1j
		for n in range(N):
			o += s[n] * np.exp(-1j*2*np.pi*k*n/N)
		S.append(o)
	return S
	
print ("DFT of x(n)\n",DFT(x))
print()
print ("DFT of h(n)\n",DFT(h))

plt.stem(range(0,N),x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()

#If using termux
#plt.savefig('../figs/ee18btech11011_fig1.pdf')
#plt.savefig('../figs/ee18btech11011_fig1.eps')
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11011_fig1.pdf"))
#else
plt.show()

plt.stem(range(0,M),h)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()

#If using termux
#plt.savefig('../figs/ee18btech11011_fig2.pdf')
#plt.savefig('../figs/ee18btech11011_fig2.pdf')
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11011_fig2.pdf"))
#else
plt.show()

plt.stem(range(0,N),DFT(x))
plt.xlabel('$n$')
plt.ylabel('$DFT(x)$')
plt.grid()

#If using termux
#plt.savefig('../figs/ee18btech11011_fig3.pdf')
#plt.savefig('../figs/ee18btech11011_fig3.eps')
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11011_fig3.pdf"))
#else
plt.show()

plt.stem(range(0,M),DFT(h))
plt.xlabel('$n$')
plt.ylabel('$DFT(h)$')
plt.grid()

#If using termux
#plt.savefig('../figs/ee18btech11011_fig4.pdf')
#plt.savefig('../figs/ee18btech11011_fig4.eps')
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11011_fig4.pdf"))
#else
plt.show()
