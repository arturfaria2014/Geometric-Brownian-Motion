import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = 50
dt = 0.1
price_0 = 100
price=pd.DataFrame()
np.random.seed(1)


def mu(t):
    return t


for sigma in np.arange(1,2, 0.2):
    step=np.exp((mu(1)-sigma**2)*dt)*np.exp(sigma*np.random.normal(0,np.sqrt(dt), (1,n)))
    temp=pd.DataFrame(price_0*step.cumprod())
    price=pd.concat([price, temp], axis=1)

price.columns = np.arange(1,2,0.2)
plt.plot(price)
plt.legend(price.columns)
plt.xlabel('t')
plt.ylabel('price')
plt.title("Geometric Brownian Motion Simulation with\n mu="+str(mu(1)))
plt.show()
