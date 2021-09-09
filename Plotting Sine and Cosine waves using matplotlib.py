import matlpotlib.pyplot as plt
import numpy as np
matplotlib inline 
x = np.arrange(0,4*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()
x = np.arange(0,4*np.pi-1,0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)               
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list
plt.show()
