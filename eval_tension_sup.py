from math import * 
import numpy as np 
import matplotlib.pyplot as plt 

##rayon critique du radeau 
def rayon_critique(e,psable,phuile,peau,gamma): 
    A=3*e*psable/(2*(peau-phuile)) 
    return(A*(1-(sqrt(1-(4*gamma*(peau-phuile))/(3*(e**2)*(psable**2)*9.8))))) 

X=np.linspace(20*10**(-3),100*10**(-3),1000) 
Y=[rayon_critique(10**(-3),1480,923,10**3,g) for g in X] 
plt.clf() 
plt.xlabel('tension superficielle') 
plt.ylabel('rayon critique') 
plt.plot(X,Y) 
plt.show()