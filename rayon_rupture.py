from math import *
import numpy as np
import matplotlib.pyplot as plt
##rayon critique du radeau
def rayon_critique(e,psable,phuile,peau,gamma):
    A=3*e*psable/(2*(peau-phuile))
    return(A*(1-(sqrt(1-(4*gamma*(peau-phuile))/(3*(e**2)*(psable**2)*9.8)))))

X=np.linspace(10**(-3),0.01,1000)
Y=[rayon_critique(e,2.6*10**3,0.923*10**3,10**3,24*10**(-3)) for e in X]
plt.xlabel('épaisseur e')
plt.ylabel('rayon critique')
plt.plot(X,Y)
plt.show()
##rayon critique pour différente tension superficielle (objectif perso)
X=np.linspace(20*10**(-3),100*10**(-3),1000)
Y=[rayon_critique(10**(-3),1480,923,10**3,g) for g in X]
plt.clf()
plt.xlabel('tension superficielle')
plt.ylabel('rayon critique')
plt.plot(X,Y)
plt.show()
#on voit que plus le coefficient de tension superficiel est grand, plus le rayon critique est grand, donc n'explique pas pourquoi ca pourrait mieux marcher avec des tensioactifs
