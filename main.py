import option as op
import asset as asset

import matplotlib.pyplot as plt 
import numpy as np

K = 100
payoff_call = lambda x,K : (x-K)*(x > K)
payoff_put = lambda x,K : (K-x)*(x < K)

#Call = op.option(payoff = payoff_call)

S = asset.asset()

call = op.option(S = S, payoff = payoff_call)
put = op.option(S = S, payoff = payoff_put)


mc_arr = [500,800,1000,2000,5000,7000,10000]
price_arr = []
IC_arr = []

for MC in mc_arr:
 price, IC = call.price(0,MC)
 price_arr.append(price)
 IC_arr.append(IC)
 
IC_arr = np.array(IC_arr)
 
plt.plot(mc_arr,price_arr, label = "price")
plt.scatter(mc_arr,price_arr)

plt.plot(mc_arr, IC_arr[:,0], color = 'r', label = "IC")
plt.plot(mc_arr, IC_arr[:,1], color = 'r')

plt.scatter(mc_arr, IC_arr[:,0], color = 'r')
plt.scatter(mc_arr, IC_arr[:,1], color = 'r')

plt.xlabel("MC : nb itérations Monte-Carlo") ; plt.ylabel("price")
plt.grid() ; plt.legend(); plt.show()
