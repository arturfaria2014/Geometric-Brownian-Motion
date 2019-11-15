import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = 50  #total number of time slices    
dt = 0.1 # unit time step of 0.1 out of 50
price_0 = 100 #initial price of the brownian motion
price=pd.DataFrame() # creating a data set for the price movement
np.random.seed(1) 

# the mean as a function of time, for simplicity we made a linear relationship between average and time
#as time increases so does the mean value of our brownian motion
def mu(t):
    return t

# we generate a unique value for each standard deviation, in this case we will vary the standard deviation between 1 and 2
# with steps of 0.2 in between unique standard deviations
for sigma in np.arange(1,2, 0.2):
    step=np.exp((mu(1)-sigma**2)*dt)*np.exp(sigma*np.random.normal(0,np.sqrt(dt), (1,n)))#for each step generate a value for
    temp=pd.DataFrame(price_0*step.cumprod())                                            # the brownian motion with expression of a standard
    price=pd.concat([price, temp], axis=1)                                               # of a standard normal distribution

price.columns = np.arange(1,2,0.2)
plt.plot(price)
plt.legend(price.columns)
plt.xlabel('t')
plt.ylabel('price')
plt.title("Geometric Brownian Motion Simulation with\n mu="+str(mu(1)))
plt.show()
