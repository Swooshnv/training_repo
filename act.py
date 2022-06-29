import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=[1,2,3]
y=[5,6,7]
plt.figure(figsize=(16,9),dpi=100)
num=np.arange(0,5,0.5)
plt.plot(num[:5],num[:5]**2,'r*-',label='x^2')
plt.plot(num[4:],num[4:]**2, 'gD--')
print(num)
plt.plot(x,y,'mo--',label='2x Line')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('My Graph')
plt.legend()
plt.savefig('myplot.png')
plt.show()
